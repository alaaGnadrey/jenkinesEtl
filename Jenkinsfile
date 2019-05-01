pipeline {
agent any
    stages {
            stage('Prepare') {
                steps {
                    withPythonEnv('python') {
                        // Creates the virtualenv before proceeding
                        echo 'install requirements..'
                        sh 'pip install -r resources/requirements.txt'    
                    }
                }
            }
            stage('Execute') {
                steps {
                    echo 'Executing..'
                    withPythonEnv('python') {
                    sh 'python -u -m resources.pipelines.poc_pipeline.execute_step1'   
                    sh 'python -u -m resources.pipelines.poc_pipeline.execute_step2'   
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
}