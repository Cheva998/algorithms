class Person {
            public $isAlive = true;
            public $firstname;
            public $lastname;
            public $age;
            
            public function __constructor($firstname, $lastname, $age) {
                $this->firstname = $firstname;
                $this->lastname = $lastname;
                $this->age = $age;
            }
            public function greet() {
                return "Hello, my name is " . $this->firstname . " " . $this->lastname . 
                ". Nice to meet you! :-)";
            }
        }
        $teacher = new Person("boring", "12345", 12345);
        $student = new Person("Sebas", "du1", 34);
        echo $teacher->isAlive;
        echo $student->age;
        echo $student -> greet();