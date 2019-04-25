pipeline {
    agent any

    stages {
        stage('Prepare') {
            steps {
                withPythonEnv('some-python-installation') {
                    // Creates the virtualenv before proceeding
                    echo 'install requirements..'
                    sh 'pip install -r resources/requirements.txt'    
                }
            }
        }
        stage('Execute') {
            steps {
                echo 'Executing..'
                withPythonEnv('some-python-installation') {
                   sh 'python -u -m resources.executors.sql_executer'      
                }
            } 
        }
        stage('Cleaning') {
            steps {
                echo 'Cleaning....'
            }
        }
    }
}