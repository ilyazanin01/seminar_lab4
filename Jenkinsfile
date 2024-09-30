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
		if (fileExists('sample_tests.py321')) {
			try {
                    		sh 'python -m unittest sample_tests.py123' // Or use 'python -m unittest discover' 
  	                } catch (err) {
                    		echo "Unit tests failed: ${err}"
			   	currentBuild.result = 'FAILURE'
                	}
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

