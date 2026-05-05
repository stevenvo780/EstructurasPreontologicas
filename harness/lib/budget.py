"""Cuotas de detención: tiempo y tokens. Cada subagente y cada pasada las respeta."""
from __future__ import annotations
import time
from dataclasses import dataclass, field


@dataclass
class Budget:
    max_seconds: float
    max_tokens: int = 0
    started_at: float = field(default_factory=time.time)
    consumed_tokens: int = 0
    consecutive_no_progress: int = 0
    max_no_progress: int = 3

    def elapsed(self) -> float:
        return time.time() - self.started_at

    def remaining_seconds(self) -> float:
        return max(0.0, self.max_seconds - self.elapsed())

    def consume_tokens(self, n: int) -> None:
        self.consumed_tokens += n

    def mark_progress(self) -> None:
        self.consecutive_no_progress = 0

    def mark_no_progress(self) -> None:
        self.consecutive_no_progress += 1

    def stop_required(self) -> tuple[bool, str]:
        if self.elapsed() >= self.max_seconds:
            return True, f"time budget exhausted ({self.max_seconds}s)"
        if self.max_tokens and self.consumed_tokens >= self.max_tokens:
            return True, f"token budget exhausted ({self.max_tokens})"
        if self.consecutive_no_progress >= self.max_no_progress:
            return True, f"no-convergence after {self.max_no_progress} iterations"
        return False, ""
