pipeline {
    agent any
    stages {
        stage('Build docker image'){
            steps{
                sh 'docker build -t mikehemli/flask-selenium-app .'
            }
        }
        stage('Run & Test') {
            agent {
                docker {
                    image "mikehemli/flask-selenium-app"
                    reuseNode true
                }
            }
            steps {
                sh 'python3 /app/main_scores.py &'
                sh 'sleep 30'
                sh 'python3 e2e.py'
            }
        }
    }
}