pipeline {
    agent any 
    stages {
        stage('Checkout') {
            steps {
                git branch:'main', url: 'https://github.com/ilyazanin01/seminar_lab4.git' 
            }
        }
        stage('Build') {
            steps {
                // Install dependencies if necessary
                echo 'Buliding...'
            }
        }
        stage('Test') {
            steps {
                // Run your unit tests
            	sh 'python3 -m unittest sample_tests.py' // Or use 'python -m unittest discover' 
            }
        }
    }
    post {
        always {
		echo 'I will always say Hello again!'
        }
    }
}

