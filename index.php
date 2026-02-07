<!-- <?php

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


// interface Rule {
//     public function evaluate(array $data): string;
// }

// class StruggleRule implements Rule {
//     public function evaluate(array $data): string {
//         return $data['attempts'] > 3 ? "Struggling" : "Normal";
//     }
// }

// $rule = new StruggleRule();
// echo $rule->evaluate(['attempts' => 5]); -->


// trait Logger {
//     public function log(string $message): void {
//         echo "[LOG] " . $message . PHP_EOL;
//     }
// }

// class Chatbot {
//     use Logger;
// }

// $bot = new Chatbot();
// $bot->log("User is struggling on Array topic");


// $scores = [60, 70, 80, 50, 90];

// $average = array_sum($scores) / count($scores);

// $status = $average < 70 ? "Low Performance" : "High Performance";

// echo "Average: $average - Status: $status";


// <?php

// function calculateAccuracy(int $correct, int $total): float {
//     if ($total === 0) {
//         throw new Exception("Total questions cannot be zero");
//     }
//     return $correct / $total;
// }

// try {
//     echo calculateAccuracy(5, 0);
// } catch (Exception $e) {
//     echo $e->getMessage();
// // }


// <?php

// function detectLearningState(int $attempts, int $timeSpent): string {
//     if ($attempts > 3 && $timeSpent > 300) {
//         return "Struggling";
//     }
//     if ($attempts > 5 && $timeSpent < 60) {
//         return "Gaming The System";
//     }
//     return "Normal";
// }

// echo detectLearningState(6, 40);


// class Score {
//     private int $value;

//     public function __construct(int $value) {
//         if ($value < 0 || $value > 100) {
//             throw new InvalidArgumentException("Invalid score");
//         }
//         $this->value = $value;
//     }

//     public function isPassed(): bool {
//         return $this->value >= 75;
//     }
// }

// $score = new Score(82);
// echo $score->isPassed() ? "Passed" : "Failed";


// <?php

// interface PerformanceStrategy {
//     public function evaluate(array $data): string;
// }

// class IdealStrategy implements PerformanceStrategy {
//     public function evaluate(array $data): string {
//         return $data['accuracy'] > 85 ? "Ideal" : "Normal";
//     }
// }

// $strategy = new IdealStrategy();
// echo $strategy->evaluate(['accuracy' => 90]);


// class StrategyFactory {
//     public static function make(string $type): PerformanceStrategy {
//         return match ($type) {
//             'ideal' => new IdealStrategy(),
//             default => throw new Exception("Unknown strategy")
//         };
//     }
// }

// $strategy = StrategyFactory::make('ideal');
// echo $strategy->evaluate(['accuracy' => 88]);

// <?php

// class StudentDTO {
//     public function __construct(
//         public string $name,
//         public int $attempts,
//         public int $timeSpent
//     ) {}
// }

// $dto = new StudentDTO("Dicky", 4, 350);
// print_r($dto);


// <?php

$students = [
    ['name' => 'A', 'score' => 60],
    ['name' => 'B', 'score' => 85],
    ['name' => 'C', 'score' => 72],
];

$highPerformers = array_filter($students, fn($s) => $s['score'] >= 75);

print_r($highPerformers);
