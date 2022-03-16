pipeline {
  agent {
    kubernetes {
      yamlFile 'KubernetesBuilder.yaml'
    }
  }
  stages {
    stage('Release') {
      steps {
        checkout scm
        container('kaniko') {
          sh 'ulimit -n 10000'
          sh '/kaniko/executor -f Dockerfile --destination=docker.ultimaengineering.io/student-project-api:${BRANCH_NAME}-${BUILD_NUMBER} --destination=docker.ultimaengineering.io/student-project-api:latest'
        }
      }
    }
  }
}