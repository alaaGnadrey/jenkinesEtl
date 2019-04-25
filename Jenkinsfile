pipeline {
    agent any

    stages {
        stage('Prepare') {
            steps {
                echo 'install requirements..'
                sh 'pip install psycopg2'    
            }
        }
        stage('Execute') {
            steps {
                echo 'Executing..'
                sh 'python -u -m resources.executors.sql_executer'      
            } 
        }
        stage('Cleaning') {
            steps {
                echo 'Cleaning....'
            }
        }
    }
}