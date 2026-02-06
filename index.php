<?php

class Student {
    private string $name;
    private int $score;

    public function __construct(string $name, int $score) {
        $this->name = $name;
        $this->score = $score;
    }

    public function getPerformance(): string {
        return $this->score >= 75 ? "High Performance" : "Low Performance";
    }
}

$student = new Student("Dicky", 70);
echo $student->getPerformance();
