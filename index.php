<?php

// class Student {
//     private string $name;
//     private int $score;

//     public function __construct(string $name, int $score) {
//         $this->name = $name;
//         $this->score = $score;
//     }

//     public function getPerformance(): string {
//         return $this->score >= 75 ? "High Performance" : "Low Performance";
//     }
// }

// $student = new Student("Dicky", 70);
// echo $student->getPerformance();

// class Performance {
//     public function category(): string {
//         return "General";
//     }
// }

// class LowPerformance extends Performance {
//     public function category(): string {
//         return "Struggling";
//     }
// }

// $perf = new LowPerformance();
// echo $perf->category();


interface Rule {
    public function evaluate(array $data): string;
}

class StruggleRule implements Rule {
    public function evaluate(array $data): string {
        return $data['attempts'] > 3 ? "Struggling" : "Normal";
    }
}

$rule = new StruggleRule();
echo $rule->evaluate(['attempts' => 5]);
