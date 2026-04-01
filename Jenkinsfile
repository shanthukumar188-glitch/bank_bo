pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t bank-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop bank-container || true'
                sh 'docker rm bank-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name bank-container bank-app'
            }
        }
    }
}
