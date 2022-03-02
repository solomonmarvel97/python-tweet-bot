pipeline {
    agent any 
    stages {
        stages("checkout") {
            steps {
                echo 'checking out our app'
            }
        }

        stages("build") {
            steps {
                echo 'building our application'
            }
        }

        stages("test") {
            steps {
                echo 'testing our application'
            }
        }

        stages("deploy") {
            steps {
                echo 'deploying our application'
            }
        }

        stages("cleanup") {
            steps {
                echo 'cleaning up our jenkins instance'
            }
        }
        
        stages("alaways") {
            steps {
                echo 'Always run this option here'
            }
        }
        
    }
}
