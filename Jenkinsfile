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
		try {
                    // Run your unit tests
                    sh 'python -m unittest sample_tests.py' // Or use 'python -m unittest discover' 
                } catch (err) {
                    // Handle the exception
                    echo "Unit tests failed: ${err}"
		    currentBuild.result = 'FAILURE'
                    // Optional: Send the error message to a reporting tool 
                }
            }
        }
    }
    post {
        always {
		echo 'I will always say Hello again!'
        }
    }
}

