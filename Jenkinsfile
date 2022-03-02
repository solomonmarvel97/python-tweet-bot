pipeline {
    agent any 
    environment {
        NEW_VERSION = '1.0.0'
        SERVER_CREDENTIALS = credentials('')
    }
    stages {
        stage("checkout") {
            steps {
                echo 'checking out our app'
            }
        }

        stage("build") {
            steps {
                echo "building the application"
                echo "building version ${NEW_VERSION}"
                echo 'building our application'
            }
        }

        stage("test") {
            steps {
                echo 'testing our application'
            }
        }

        stage("deploy") {
            steps {
                echo 'deploying our application'
            }
        }

        stage("cleanup") {
            steps {
                echo 'cleaning up our jenkins instance'
            }
        }
        
        stage("alaways") {
            steps {
                echo 'Always run this option here'
            }
        }
        
    }
    post {
        always {
        }
        success {
        }
        failure {
        }
    }
}
