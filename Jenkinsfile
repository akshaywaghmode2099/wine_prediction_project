pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/akshaywaghmode2099/wine_prediction_project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t wine_quality_app:latest .'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'docker run -d -p 5000:5000 --name wine_quality_app_container wine_quality_app:latest || docker start wine_quality_app_container'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}
