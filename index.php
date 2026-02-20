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

// $students = [
//     ['name' => 'A', 'score' => 60],
//     ['name' => 'B', 'score' => 85],
//     ['name' => 'C', 'score' => 72],
// ];

// $highPerformers = array_filter($students, fn($s) => $s['score'] >= 75);

// print_r($highPerformers);


// <?php

// class LearningException extends Exception {}

// function validateAttempts(int $attempts): void {
//     if ($attempts > 10) {
//         throw new LearningException("Suspicious activity detected");
//     }
// }

// try {
//     validateAttempts(12);
// } catch (LearningException $e) {
//     echo $e->getMessage();
// }


// <?php

// class AdaptiveEngine {
//     public function decide(int $attempts, int $timeSpent): string {
//         return match (true) {
//             $attempts > 5 && $timeSpent > 300 => "Struggling",
//             $attempts > 5 && $timeSpent < 60  => "Gaming The System",
//             default => "Normal"
//         };
//     }
// }

// $engine = new AdaptiveEngine();
// echo $engine->decide(6, 45);


// <?php

class PerformanceService {
    public function classify(int $score): string {
        if ($score >= 85) return "Ideal";
        if ($score >= 70) return "Normal";
        return "Struggling";
    }
}

$service = new PerformanceService();
echo $service->classify(68);


// <?php

// class StudentRepository {
//     private array $students = [
//         ['id' => 1, 'name' => 'A', 'score' => 60],
//         ['id' => 2, 'name' => 'B', 'score' => 85],
//     ];

//     public function findById(int $id): array {
//         foreach ($this->students as $student) {
//             if ($student['id'] === $id) {
//                 return $student;
//             }
//         }
//         throw new Exception("Student not found");
//     }
// }

// $repo = new StudentRepository();
// print_r($repo->findById(2));


// <?php

// class ChatbotEngine {
//     public function __construct(
//         public PerformanceService $service
//     ) {}

//     public function respond(int $score): string {
//         return $this->service->classify($score);
//     }
// }

// $engine = new ChatbotEngine(new PerformanceService());
// echo $engine->respond(90);


// enum PerformanceLevel: string {
//     case STRUGGLING = 'Struggling';
//     case NORMAL = 'Normal';
//     case IDEAL = 'Ideal';
// }

// function levelFromScore(int $score): PerformanceLevel {
//     return match (true) {
//         $score < 70 => PerformanceLevel::STRUGGLING,
//         $score < 85 => PerformanceLevel::NORMAL,
//         default => PerformanceLevel::IDEAL
//     };
// }

// echo levelFromScore(88)->value;


// class RulePipeline {
//     private array $rules = [];

//     public function add(callable $rule): self {
//         $this->rules[] = $rule;
//         return $this;
//     }

//     public function run(array $data): string {
//         foreach ($this->rules as $rule) {
//             $result = $rule($data);
//             if ($result !== null) return $result;
//         }
//         return "Normal";
//     }
// }

// $pipeline = (new RulePipeline())
//     ->add(fn($d) => $d['attempts'] > 5 ? "Struggling" : null)
//     ->add(fn($d) => $d['time'] < 60 ? "Gaming" : null);

// echo $pipeline->run(['attempts' => 6, 'time' => 40]);


// class RequestValidator {
//     public static function validate(array $data): void {
//         if (!isset($data['attempts'], $data['time'])) {
//             throw new Exception("Invalid request data");
//         }
//     }
// }

// try {
//     RequestValidator::validate(['attempts' => 3]);
// } catch (Exception $e) {
//     echo $e->getMessage();
// }


// class AdaptiveDecisionEngine {
//     public function decide(array $data): string {
//         RequestValidator::validate($data);

//         return match (true) {
//             $data['attempts'] > 5 && $data['time'] > 300 => "Struggling",
//             $data['attempts'] > 5 && $data['time'] < 60  => "Gaming The System",
//             $data['score'] >= 85                        => "Ideal",
//             default                                     => "Normal"
//         };
//     }
// }

// $engine = new AdaptiveDecisionEngine();
// echo $engine->decide([
//     'attempts' => 6,
//     'time' => 45,
//     'score' => 78
// ]);

// class LearningDataDTO {
//     public function __construct(
//         public int $attempts,
//         public int $timeSpent,
//         public int $score
//     ) {}
// }

// $data = new LearningDataDTO(4, 120, 80);
// var_dump($data);


// interface Rule {
//     public function check(LearningDataDTO $data): ?string;
// }

// class StrugglingRule implements Rule {
//     public function check(LearningDataDTO $data): ?string {
//         return ($data->attempts > 5 && $data->score < 70)
//             ? "Struggling"
//             : null;
//     }
// }

// $rule = new StrugglingRule();
// echo $rule->check(new LearningDataDTO(6, 200, 60));


// class RuleManager {
//     private array $rules = [];

//     public function addRule(Rule $rule): void {
//         $this->rules[] = $rule;
//     }

//     public function evaluate(LearningDataDTO $data): string {
//         foreach ($this->rules as $rule) {
//             if ($result = $rule->check($data)) {
//                 return $result;
//             }
//         }
//         return "Normal";
//     }
// }

// $manager = new RuleManager();
// $manager->addRule(new StrugglingRule());

// echo $manager->evaluate(new LearningDataDTO(6, 200, 60));


// interface FeedbackStrategy {
//     public function generate(): string;
// }

// class BeginnerFeedback implements FeedbackStrategy {
//     public function generate(): string {
//         return "Pelajari ulang konsep dasar sebelum lanjut.";
//     }
// }

// class AdvancedFeedback implements FeedbackStrategy {
//     public function generate(): string {
//         return "Kamu siap ke materi lanjutan.";
//     }
// }

// function feedbackByLevel(string $level): FeedbackStrategy {
//     return match ($level) {
//         "Struggling" => new BeginnerFeedback(),
//         default => new AdvancedFeedback()
//     };
// }

// echo feedbackByLevel("Struggling")->generate();


// class ActivityLogger {
//     public static function log(string $message): void {
//         file_put_contents(
//             'activity.log',
//             date('Y-m-d H:i:s') . " - $message\n",
//             FILE_APPEND
//         );
//     }
// }

// ActivityLogger::log("Student failed algorithm quiz");


// $students = [
//     new LearningDataDTO(3, 100, 90),
//     new LearningDataDTO(7, 400, 60),
//     new LearningDataDTO(5, 150, 75),
// ];

// $averageScore = array_sum(
//     array_map(fn($s) => $s->score, $students)
// ) / count($students);

// echo "Average score: $averageScore";


// class RecommendationEngine {
//     public function recommend(LearningDataDTO $data): string {
//         if ($data->score < 70) {
//             return "Materi Remedial + Contoh Visual";
//         }

//         if ($data->timeSpent < 60) {
//             return "Latihan Lebih Banyak";
//         }

//         return "Lanjut ke Materi Berikutnya";
//     }
// }

// $engine = new RecommendationEngine();
// echo $engine->recommend(new LearningDataDTO(3, 45, 75));


// class InvalidLearningDataException extends Exception {}

// class LearningValidator {
//     public static function validate(int $score, int $attempts): void {
//         if ($score < 0 || $score > 100) {
//             throw new InvalidLearningDataException("Score must be 0–100.");
//         }

//         if ($attempts < 0) {
//             throw new InvalidLearningDataException("Attempts cannot be negative.");
//         }
//     }
// }

// try {
//     LearningValidator::validate(120, 3);
// } catch (InvalidLearningDataException $e) {
//     echo $e->getMessage();
// }


// interface StudentRepositoryInterface {
//     public function findById(int $id): array;
// }

// class StudentRepository implements StudentRepositoryInterface {

//     private array $students = [
//         1 => ['name' => 'Dicky', 'score' => 80],
//         2 => ['name' => 'Budi', 'score' => 60],
//     ];

//     public function findById(int $id): array {
//         return $this->students[$id] ?? [];
//     }
// }

// $repo = new StudentRepository();
// print_r($repo->findById(1));

// class AdaptiveService {

//     public function analyze(array $student): string {
//         if ($student['score'] < 70) {
//             return "Remedial Algorithm Material";
//         }

//         return "Next Level Material";
//     }
// }

// $service = new AdaptiveService();
// echo $service->analyze(['score' => 65]);

// class Middleware {

//     public static function handle(callable $next) {
//         echo "Logging activity...\n";
//         return $next();
//     }
// }

// Middleware::handle(function() {
//     return "Processing adaptive chatbot response.";
// });

// class ApiResponse {

//     public static function success($data): string {
//         return json_encode([
//             'status' => 'success',
//             'data' => $data
//         ]);
//     }

//     public static function error(string $message): string {
//         return json_encode([
//             'status' => 'error',
//             'message' => $message
//         ]);
//     }
// }

// echo ApiResponse::success(['recommendation' => 'Remedial']);


// class ChatbotController {

//     public function __construct(
//         private AdaptiveService $service
//     ) {}

//     public function handle(array $student): string {
//         return $this->service->analyze($student);
//     }
// }

// $controller = new ChatbotController(new AdaptiveService());
// echo $controller->handle(['score' => 85]);



// class AnalyticsEngine {

//     public function calculatePerformance(int $score, int $timeSpent): float {
//         $scoreWeight = 0.7;
//         $timeWeight  = 0.3;

//         $normalizedTime = min($timeSpent / 300, 1); // max 300 sec

//         return ($score * $scoreWeight) + ($normalizedTime * 100 * $timeWeight);
//     }
// }

// $engine = new AnalyticsEngine();
// echo $engine->calculatePerformance(80, 200);


// abstract class PerformanceCategory {
//     protected int $score;

//     public function __construct(int $score) {
//         $this->score = $score;
//     }

//     abstract public function getCategory(): string;
// }

// class LowPerformance extends PerformanceCategory {
//     public function getCategory(): string {
//         return $this->score < 50 ? "Struggling" : "Gaming the System";
//     }
// }

// class HighPerformance extends PerformanceCategory {
//     public function getCategory(): string {
//         return $this->score > 90 ? "Ideal" : "Normal";
//     }
// }

// $student = new LowPerformance(40);
// echo $student->getCategory();



// interface ResponseStrategy {
//     public function execute(): string;
// }

// class ArrayDefinitionStrategy implements ResponseStrategy {
//     public function execute(): string {
//         return "Array adalah struktur data yang menyimpan banyak nilai dalam satu variabel.";
//     }
// }

// class AlgorithmHintStrategy implements ResponseStrategy {
//     public function execute(): string {
//         return "Coba perhatikan kembali indeks array dimulai dari 0.";
//     }
// }

// class ChatbotContext {
//     private ResponseStrategy $strategy;

//     public function setStrategy(ResponseStrategy $strategy) {
//         $this->strategy = $strategy;
//     }

//     public function respond(): string {
//         return $this->strategy->execute();
//     }
// }

// $chatbot = new ChatbotContext();
// $chatbot->setStrategy(new ArrayDefinitionStrategy());
// echo $chatbot->respond();


// class PerformanceFactory {

//     public static function create(int $score): PerformanceCategory {
//         if ($score < 70) {
//             return new LowPerformance($score);
//         }
//         return new HighPerformance($score);
//     }
// }

// $category = PerformanceFactory::create(95);
// echo $category->getCategory();


// interface Observer {
//     public function update(string $category): void;
// }

// class NotificationObserver implements Observer {
//     public function update(string $category): void {
//         if ($category === "Struggling") {
//             echo "Trigger chatbot bantuan materi dasar.";
//         }
//     }
// }

// class PerformanceSubject {
//     private array $observers = [];

//     public function attach(Observer $observer) {
//         $this->observers[] = $observer;
//     }

//     public function notify(string $category) {
//         foreach ($this->observers as $observer) {
//             $observer->update($category);
//         }
//     }
// }

// $subject = new PerformanceSubject();
// $subject->attach(new NotificationObserver());
// $subject->notify("Struggling");


// class EventDispatcher {

//     private array $listeners = [];

//     public function listen(string $event, callable $callback) {
//         $this->listeners[$event][] = $callback;
//     }

//     public function dispatch(string $event, $payload = null) {
//         if (!empty($this->listeners[$event])) {
//             foreach ($this->listeners[$event] as $listener) {
//                 $listener($payload);
//             }
//         }
//     }
// }

// $dispatcher = new EventDispatcher();

// $dispatcher->listen("student.struggling", function($data) {
//     echo "Mahasiswa {$data['name']} mengalami kesulitan.";
// });

// $dispatcher->dispatch("student.struggling", ['name' => 'Dicky']);

// class Database {

//     private static ?PDO $instance = null;

//     public static function connect(): PDO {
//         if (self::$instance === null) {
//             self::$instance = new PDO(
//                 "mysql:host=localhost;dbname=pseudolearn",
//                 "root",
//                 ""
//             );
//             self::$instance->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
//         }
//         return self::$instance;
//     }
// }

// $db = Database::connect();
// echo "Database connected.";


// session_start();

// class SessionTracker {

//     public static function trackAttempt(int $score) {
//         $_SESSION['attempts'][] = $score;
//     }

//     public static function averageScore(): float {
//         return array_sum($_SESSION['attempts']) / count($_SESSION['attempts']);
//     }
// }

// SessionTracker::trackAttempt(60);
// SessionTracker::trackAttempt(70);

// echo SessionTracker::averageScore();



// trait Timestampable {
//     public function currentTimestamp(): string {
//         return date('Y-m-d H:i:s');
//     }
// }

// class LearningLog {
//     use Timestampable;

//     public function create(string $message): string {
//         return $this->currentTimestamp() . " - " . $message;
//     }
// }

// $log = new LearningLog();
// echo $log->create("Student completed quiz.");


// class RecommendationBuilder {
//     private array $data = [];

//     public function setScore(int $score): self {
//         $this->data['score'] = $score;
//         return $this;
//     }

//     public function setAttempts(int $attempts): self {
//         $this->data['attempts'] = $attempts;
//         return $this;
//     }

//     public function build(): string {
//         if ($this->data['score'] < 70) {
//             return "Remedial Package";
//         }
//         return "Advanced Package";
//     }
// }

// $result = (new RecommendationBuilder())
//     ->setScore(65)
//     ->setAttempts(5)
//     ->build();

// echo $result;


// class Config {

//     private static array $settings = [
//         'pass_score' => 75,
//         'max_attempts' => 5
//     ];

//     public static function get(string $key) {
//         return self::$settings[$key] ?? null;
//     }
// }

// echo Config::get('pass_score');


// class RateLimiter {

//     private array $attempts = [];

//     public function hit(string $user): bool {
//         $this->attempts[$user] = ($this->attempts[$user] ?? 0) + 1;

//         if ($this->attempts[$user] > 5) {
//             return false; // Block user
//         }
//         return true;
//     }
// }

// $limiter = new RateLimiter();
// echo $limiter->hit("student_1") ? "Allowed" : "Blocked";


// class QueryBuilder {

//     private string $table;
//     private array $conditions = [];

//     public function table(string $table): self {
//         $this->table = $table;
//         return $this;
//     }

//     public function where(string $column, string $operator, $value): self {
//         $this->conditions[] = "$column $operator '$value'";
//         return $this;
//     }

//     public function toSql(): string {
//         $where = implode(" AND ", $this->conditions);
//         return "SELECT * FROM {$this->table} WHERE $where";
//     }
// }

// $sql = (new QueryBuilder())
//     ->table('students')
//     ->where('score', '>', 70)
//     ->where('attempts', '<', 5)
//     ->toSql();

// echo $sql;



// interface StudentState {
//     public function handle(): string;
// }

// class StrugglingState implements StudentState {
//     public function handle(): string {
//         return "Provide basic learning material.";
//     }
// }

// class IdealState implements StudentState {
//     public function handle(): string {
//         return "Unlock advanced challenges.";
//     }
// }

// class StudentContext {
//     private StudentState $state;

//     public function setState(StudentState $state) {
//         $this->state = $state;
//     }

//     public function process(): string {
//         return $this->state->handle();
//     }
// }

// $context = new StudentContext();
// $context->setState(new StrugglingState());
// echo $context->process();


// class PerformanceEngine {

//     public function evaluate(int $score, int $timeSpent, int $attempts): string {

//         $weighted = ($score * 0.6) + (min($timeSpent, 300)/300 * 100 * 0.2) + ((5 - $attempts) * 20 * 0.2);

//         if ($weighted >= 85) return "Ideal";
//         if ($weighted >= 70) return "Normal";
//         return "Struggling";
//     }
// }

// $engine = new PerformanceEngine();
// echo $engine->evaluate(80, 200, 3);

// interface ScoreAnalyzer {
//     public function analyzeScore(int $score): string;
// }

// interface TimeAnalyzer {
//     public function analyzeTime(int $time): string;
// }

// class LearningAnalyzer implements ScoreAnalyzer, TimeAnalyzer {

//     public function analyzeScore(int $score): string {
//         return $score >= 75 ? "Pass" : "Fail";
//     }

//     public function analyzeTime(int $time): string {
//         return $time < 60 ? "Too Fast" : "Normal";
//     }
// }

// $analyzer = new LearningAnalyzer();
// echo $analyzer->analyzeScore(80);



// interface AdaptiveRule {
//     public function apply(array $data): ?string;
// }

// class LowScoreRule implements AdaptiveRule {
//     public function apply(array $data): ?string {
//         return $data['score'] < 70 ? "Remedial" : null;
//     }
// }

// class AdaptiveEngine {

//     private array $rules = [];

//     public function addRule(AdaptiveRule $rule): void {
//         $this->rules[] = $rule;
//     }

//     public function process(array $data): string {
//         foreach ($this->rules as $rule) {
//             if ($result = $rule->apply($data)) {
//                 return $result;
//             }
//         }
//         return "Next Level";
//     }
// }

// $engine = new AdaptiveEngine();
// $engine->addRule(new LowScoreRule());

// echo $engine->process(['score' => 65]);

// class SubmitScoreCommand {
//     public function __construct(
//         public int $studentId,
//         public int $score
//     ) {}
// }

// class SubmitScoreHandler {
//     public function handle(SubmitScoreCommand $command): string {
//         return "Score {$command->score} saved for student {$command->studentId}";
//     }
// }

// $handler = new SubmitScoreHandler();
// echo $handler->handle(new SubmitScoreCommand(1, 85));


// final class Score {

//     private int $value;

//     public function __construct(int $value) {
//         if ($value < 0 || $value > 100) {
//             throw new InvalidArgumentException("Invalid score.");
//         }
//         $this->value = $value;
//     }

//     public function value(): int {
//         return $this->value;
//     }
// }

// $score = new Score(88);
// echo $score->value();


// class StudentStrugglingEvent {
//     public function __construct(public int $studentId) {}
// }

// class EventBus {

//     private array $listeners = [];

//     public function subscribe(string $event, callable $listener) {
//         $this->listeners[$event][] = $listener;
//     }

//     public function publish(object $event) {
//         $class = get_class($event);
//         foreach ($this->listeners[$class] ?? [] as $listener) {
//             $listener($event);
//         }
//     }
// }

// $bus = new EventBus();

// $bus->subscribe(StudentStrugglingEvent::class, function($event) {
//     echo "Trigger chatbot support for student {$event->studentId}";
// });

// $bus->publish(new StudentStrugglingEvent(2));

// class StudentPolicy {

//     public function canAccessAdvanced(int $score): bool {
//         return $score >= 85;
//     }
// }

// $policy = new StudentPolicy();
// echo $policy->canAccessAdvanced(90) ? "Access Granted" : "Denied";


// class AdaptiveDomainService {

//     public function evaluate(int $score, int $time, int $attempts): string {

//         $performanceIndex = 
//             ($score * 0.6) +
//             (min($time, 300)/300 * 100 * 0.2) +
//             ((5 - $attempts) * 20 * 0.2);

//         return match (true) {
//             $performanceIndex >= 85 => "Ideal",
//             $performanceIndex >= 70 => "Normal",
//             default => "Struggling"
//         };
//     }
// }

// $service = new AdaptiveDomainService();
// echo $serviceaefa->evaluate(78, 200, 4);

// class Student {

//     private int $id;
//     private int $score;
//     private int $attempts;

//     public function __construct(int $id, int $score, int $attempts) {
//         $this->id = $id;
//         $this->score = $score;
//         $this->attempts = $attempts;
//     }

//     public function improveScore(int $points): void {
//         $this->score = min(100, $this->score + $points);
//     }

//     public function performanceLevel(): string {
//         return $this->score >= 85 ? "Ideal" :
//                ($this->score >= 70 ? "Normal" : "Struggling");
//     }

//     public function id(): int {
//         return $this->id;
//     }
// }

// $student = new Student(1, 75, 3);
// $student->improveScore(10);
// echo $student->performanceLevel();

// interface StudentRepository {
//     public function save(Student $student): void;
//     public function find(int $id): ?Student;
// }

// class InMemoryStudentRepository implements StudentRepository {

//     private array $storage = [];

//     public function save(Student $student): void {
//         $this->storage[$student->id()] = $student;
//     }

//     public function find(int $id): ?Student {
//         return $this->storage[$id] ?? null;
//     }
// }

// $repo = new InMemoryStudentRepository();
// $repo->save(new Student(1, 80, 2));

// echo $repo->find(1)->performanceLevel();

// class EvaluateStudentUseCase {

//     public function __construct(
//         private StudentRepository $repository
//     ) {}

//     public function execute(int $studentId): string {
//         $student = $this->repository->find($studentId);

//         if (!$student) {
//             throw new Exception("Student not found");
//         }

//         return $student->performanceLevel();
//     }
// }

// $useCase = new EvaluateStudentUseCase($repo);
// echo $useCase->execute(1);


// class UnitOfWork {

//     private array $entities = [];

//     public function register(Student $student): void {
//         $this->entities[] = $student;
//     }

//     public function commit(): void {
//         foreach ($this->entities as $entity) {
//             echo "Persisting student ID: " . $entity->id() . "\n";
//         }
//         $this->entities = [];
//     }
// }

// $uow = new UnitOfWork();
// $uow->register(new Student(2, 60, 5));
// $uow->commit();


// interface Specification {
//     public function isSatisfiedBy(Student $student): bool;
// }

// class StrugglingSpecification implements Specification {
//     public function isSatisfiedBy(Student $student): bool {
//         return $student->performanceLevel() === "Struggling";
//     }
// }

// $spec = new StrugglingSpecification();
// echo $spec->isSatisfiedBy(new Student(3, 50, 4)) ? "Yes" : "No";


// class StudentImprovedEvent {
//     public function __construct(public int $studentId) {}
// }

// class StudentAggregate extends Student {

//     private array $events = [];

//     public function improveScore(int $points): void {
//         parent::improveScore($points);
//         $this->events[] = new StudentImprovedEvent($this->id());
//     }

//     public function pullEvents(): array {
//         $events = $this->events;
//         $this->events = [];
//         return $events;
//     }
// }

// $aggregate = new StudentAggregate(5, 70, 3);
// $aggregate->improveScore(20);

// foreach ($aggregate->pullEvents() as $event) {
//     echo "Event triggered for student {$event->studentId}";
// }



// class Container {

//     private array $bindings = [];

//     public function bind(string $abstract, callable $factory): void {
//         $this->bindings[$abstract] = $factory;
//     }

//     public function resolve(string $abstract) {
//         if (!isset($this->bindings[$abstract])) {
//             throw new Exception("Class not bound.");
//         }

//         return $this->bindings[$abstract]($this);
//     }
// }

// $container = new Container();

// $container->bind(StudentRepository::class, function () {
//     return new InMemoryStudentRepository();
// });

// $repo = $container->resolve(StudentRepository::class);


// abstract class ServiceProvider {
//     abstract public function register(Container $container): void;
// }

// class StudentServiceProvider extends ServiceProvider {

//     public function register(Container $container): void {
//         $container->bind(
//             StudentRepository::class,
//             fn() => new InMemoryStudentRepository()
//         );
//     }
// }

// $provider = new StudentServiceProvider();
// $provider->register($container);


// class CommandBus {

//     private array $handlers = [];

//     public function register(string $command, callable $handler): void {
//         $this->handlers[$command] = $handler;
//     }

//     public function dispatch(object $command) {
//         $class = get_class($command);

//         if (!isset($this->handlers[$class])) {
//             throw new Exception("No handler registered.");
//         }

//         return $this->handlers[$class]($command);
//     }
// }

// class UpgradeStudentCommand {
//     public function __construct(public int $studentId) {}
// }

// $bus = new CommandBus();

// $bus->register(
//     UpgradeStudentCommand::class,
//     fn($cmd) => "Student {$cmd->studentId} upgraded."
// );

// echo $bus->dispatch(new UpgradeStudentCommand(10));


// class EventStore {

//     private array $events = [];

//     public function append(object $event): void {
//         $this->events[] = $event;
//     }

//     public function all(): array {
//         return $this->events;
//     }
// }

// class ScoreSubmittedEvent {
//     public function __construct(public int $studentId, public int $score) {}
// }

// $store = new EventStore();
// $store->append(new ScoreSubmittedEvent(1, 90));

// print_r($store->all());


// class JobQueue {

//     private array $jobs = [];

//     public function push(callable $job): void {
//         $this->jobs[] = $job;
//     }

//     public function run(): void {
//         while ($job = array_shift($this->jobs)) {
//             $job();
//         }
//     }
// }

// $queue = new JobQueue();

// $queue->push(fn() => print("Sending notification...\n"));
// $queue->push(fn() => print("Updating analytics...\n"));

// $queue->run();

// class Pipeline {

//     public function process($data, array $pipes) {

//         $pipeline = array_reduce(
//             array_reverse($pipes),
//             fn($next, $pipe) =>
//                 fn($data) => $pipe($data, $next),
//             fn($data) => $data
//         );

//         return $pipeline($data);
//     }
// }

// $pipeline = new Pipeline();

// $result = $pipeline->process(
//     60,
//     [
//         fn($score, $next) => $next($score + 10),
//         fn($score, $next) => $next($score * 2),
//     ]
// );

// echo $result; // (60+10)*2


// class StudentProjection {

//     private array $readModel = [];

//     public function apply(object $event): void {

//         if ($event instanceof ScoreSubmittedEvent) {
//             $this->readModel[$event->studentId] = $event->score;
//         }
//     }

//     public function getScore(int $studentId): ?int {
//         return $this->readModel[$studentId] ?? null;
//     }
// }

// $projection = new StudentProjection();

// foreach ($store->all() as $event) {
//     $projection->apply($event);
// }

// echo $projection->getScore(1);



// class JwtService {

//     private string $secret = "super_secret_key";

//     public function generate(array $payload): string {

//         $header = base64_encode(json_encode(['alg' => 'HS256', 'typ' => 'JWT']));
//         $body   = base64_encode(json_encode($payload));

//         $signature = hash_hmac(
//             'sha256',
//             "$header.$body",
//             $this->secret,
//             true
//         );

//         return "$header.$body." . base64_encode($signature);
//     }

//     public function validate(string $token): bool {

//         [$header, $body, $signature] = explode('.', $token);

//         $expected = base64_encode(
//             hash_hmac('sha256', "$header.$body", $this->secret, true)
//         );

//         return hash_equals($expected, $signature);
//     }
// }

// $jwt = new JwtService();
// $token = $jwt->generate(['user_id' => 1]);
// echo $jwt->validate($token) ? "Valid Token" : "Invalid Token";



// <?php

// class Cache {

//     private array $store = [];

//     public function put(string $key, $value, int $ttl): void {
//         $this->store[$key] = [
//             'value' => $value,
//             'expires_at' => time() + $ttl
//         ];
//     }

//     public function get(string $key) {
//         if (!isset($this->store[$key])) return null;

//         if ($this->store[$key]['expires_at'] < time()) {
//             unset($this->store[$key]);
//             return null;
//         }

//         return $this->store[$key]['value'];
//     }
// }

// $cache = new Cache();
// $cache->put("student_1_score", 90, 10);
// echo $cache->get("student_1_score");


// class TenantResolver {

//     public function resolve(): string {
//         $host = $_SERVER['HTTP_HOST'] ?? 'default.local';

//         return explode('.', $host)[0];
//     }
// }

// $resolver = new TenantResolver();
// echo $resolver->resolve();


// interface Module {
//     public function boot(): void;
// }

// class StudentModule implements Module {
//     public function boot(): void {
//         echo "Student Module Booted\n";
//     }
// }

// class ModuleLoader {

//     private array $modules = [];

//     public function register(Module $module): void {
//         $this->modules[] = $module;
//     }

//     public function boot(): void {
//         foreach ($this->modules as $module) {
//             $module->boot();
//         }
//     }
// }

// $loader = new ModuleLoader();
// $loader->register(new StudentModule());
// $loader->boot();


// class TokenBucket {

//     private int $tokens;
//     private int $capacity;

//     public function __construct(int $capacity) {
//         $this->capacity = $capacity;
//         $this->tokens = $capacity;
//     }

//     public function consume(): bool {
//         if ($this->tokens <= 0) {
//             return false;
//         }

//         $this->tokens--;
//         return true;
//     }
// }

// $bucket = new TokenBucket(5);
// echo $bucket->consume() ? "Allowed" : "Blocked";

// class StudentResource {

//     public static function make(Student $student): array {
//         return [
//             'id' => $student->id(),
//             'performance' => $student->performanceLevel()
//         ];
//     }
// }

// $student = new Student(1, 88, 2);
// print_r(StudentResource::make($student));



// class PasswordService {

//     public function hash(string $password): string {
//         return password_hash($password, PASSWORD_BCRYPT);
//     }

//     public function verify(string $password, string $hash): bool {
//         return password_verify($password, $hash);
//     }
// }

// $service = new PasswordService();

// $hash = $service->hash("secret123");

// echo $service->verify("secret123", $hash) 
//     // ? "Password Match" 
//      : "Invalid Password";


// class ApiGateway {

//     private array $routes = [];

//     public function register(string $path, callable $handler): void {
//         $this->routes[$path] = $handler;
//     }

//     public function handle(string $path) {
//         if (!isset($this->routes[$path])) {
//             return "404 Not Found";
//         }

//         return $this->routes[$path]();
//     }
// }

// $gateway = new ApiGateway();

// $gateway->register('/students', fn() => "Student Service Response");

// echo $gateway->handle('/students');


// class MiddlewarePipeline {

//     public function handle($request, array $middlewares, callable $core) {

//         $pipeline = array_reduce(
//             array_reverse($middlewares),
//             fn($next, $middleware) =>
//                 fn($req) => $middleware($req, $next),
//             $core
//         );

//         return $pipeline($request);
//     }
// }

// $pipeline = new MiddlewarePipeline();

// $response = $pipeline->handle(
//     "REQUEST",
//     [
//         fn($req, $next) => $next($req . " | Auth OK"),
//         fn($req, $next) => $next($req . " | Logged"),
//     ],
//     fn($req) => $req . " | Controller"
// );

// echo $response;

// class CircuitBreaker {

//     private int $failures = 0;
//     private int $threshold;

//     public function __construct(int $threshold = 3) {
//         $this->threshold = $threshold;
//     }

//     public function call(callable $service) {

//         if ($this->failures >= $this->threshold) {
//             return "Service Unavailable (Open Circuit)";
//         }

//         try {
//             return $service();
//         } catch (Exception $e) {
//             $this->failures++;
//             return "Failure Recorded";
//         }
//     }
// }

// $breaker = new CircuitBreaker();

// echo $breaker->call(fn() => "External API OK");



// function retry(callable $task, int $attempts = 3) {

//     for ($i = 1; $i <= $attempts; $i++) {
//         try {
//             return $task();
//         } catch (Exception $e) {
//             if ($i === $attempts) {
//                 throw $e;
//             }
//         }
//     }
// }

// echo retry(fn() => "Success");

// class IdempotencyService {

//     private array $processed = [];

//     public function handle(string $key, callable $action) {

//         if (isset($this->processed[$key])) {
//             return "Duplicate Request Ignored";
//         }

//         $this->processed[$key] = true;

//         return $action();
//     }
// }

// $idempotency = new IdempotencyService();

// echo $idempotency->handle("txn_123", fn() => "Transaction Processed");

// class LockManager {

//     private array $locks = [];

//     public function acquire(string $key): bool {

//         if (isset($this->locks[$key])) {
//             return false;
//         }

//         $this->locks[$key] = true;
//         return true;
//     }

//     public function release(string $key): void {
//         unset($this->locks[$key]);
//     }
// }

// $lock = new LockManager();

// if ($lock->acquire("student_1")) {
//     echo "Lock Acquired\n";
//     $lock->release("student_1");
// }

// class AuditTrail {

//     private array $logs = [];

//     public function record(string $action, string $user): void {
//         $this->logs[] = [
//             'action' => $action,
//             'user' => $user,
//             'time' => date('Y-m-d H:i:s')
//         ];
//     }

//     public function all(): array {
//         return $this->logs;
//     }
// }

// $audit = new AuditTrail();
// $audit->record("Upgrade Student", "admin");

// print_r($audit->all());


// class ApiGateway {

//     private array $routes = [];

//     public function register(string $path, callable $handler): void {
//         $this->routes[$path] = $handler;
//     }

//     public function handle(string $path) {
//         if (!isset($this->routes[$path])) {
//             return "404 Not Found";
//         }

//         return $this->routes[$path]();
//     }
// }

// $gateway = new ApiGateway();

// $gateway->register('/students', fn() => "Student Service Response");

// echo $gateway->handle('/students');

// <?php

// class MiddlewarePipeline {

//     public function handle($request, array $middlewares, callable $core) {

//         $pipeline = array_reduce(
//             array_reverse($middlewares),
//             fn($next, $middleware) =>
//                 fn($req) => $middleware($req, $next),
//             $core
//         );

//         return $pipeline($request);
//     }
// }

// $pipeline = new MiddlewarePipeline();

// $response = $pipeline->handle(
//     "REQUEST",
//     [
//         fn($req, $next) => $next($req . " | Auth OK"),
//         fn($req, $next) => $next($req . " | Logged"),
//     ],
//     fn($req) => $req . " | Controller"
// );

// echo $response;

// <?php

// class CircuitBreaker {

//     private int $failures = 0;
//     private int $threshold;

//     public function __construct(int $threshold = 3) {
//         $this->threshold = $threshold;
//     }

//     public function call(callable $service) {

//         if ($this->failures >= $this->threshold) {
//             return "Service Unavailable (Open Circuit)";
//         }

//         try {
//             return $service();
//         } catch (Exception $e) {
//             $this->failures++;
//             return "Failure Recorded";
//         }
//     }
// }

// $breaker = new CircuitBreaker();

// echo $breaker->call(fn() => "External API OK");

// <?php

// function retry(callable $task, int $attempts = 3) {

//     for ($i = 1; $i <= $attempts; $i++) {
//         try {
//             return $task();
//         } catch (Exception $e) {
//             if ($i === $attempts) {
//                 throw $e;
//             }
//         }
//     }
// }

// echo retry(fn() => "Success");


// <?php

// function retry(callable $task, int $attempts = 3) {

//     for ($i = 1; $i <= $attempts; $i++) {
//         try {
//             return $task();
//         } catch (Exception $e) {
//             if ($i === $attempts) {
//                 throw $e;
//             }
//         }
//     }
// }

// echo retry(fn() => "Success");

// <?php

// class Metrics {

//     private array $counters = [];

//     public function increment(string $key): void {
//         $this->counters[$key] = ($this->counters[$key] ?? 0) + 1;
//     }

//     public function all(): array {
//         return $this->counters;
//     }
// }

// $metrics = new Metrics();
// $metrics->increment("student_upgrade_calls");
// $metrics->increment("student_upgrade_calls");

// print_r($metrics->all());


// <?php

class TraceContext {

    public static function generate(): string {
        return bin2hex(random_bytes(8));
    }
}

$requestId = TraceContext::generate();

echo "Processing request: $requestId\n";