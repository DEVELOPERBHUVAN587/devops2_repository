pipeline {
  agent any

  environment {
    DISPLAY = ":0"
    XDG_RUNTIME_DIR = "/run/user/123"
    PULSE_SERVER = "unix:/run/user/123/pulse/native"
    PULSE_LATENCY_MSEC = "60"
    SDL_AUDIODRIVER = "alsa"
  }

  stages {
    stage('📥 Checkout') {
      steps {
        echo "📥 Checking out the repository..."
        checkout scm
      }
    }

    stage('✅ Allow X11 Access') {
      steps {
        echo "🔓 Allowing Docker containers to access host display..."
        // Give X11 access to docker containers (run by Jenkins)
        sh 'xhost +local:docker'
      }
    }

    stage('🐳 Build Docker Image') {
      steps {
        echo "🐳 Building Docker image..."
        sh '''
          docker build -t email-game -f docker/Dockerfile .
        '''
      }
    }

    stage('🕹️ Run the Game (GUI + Sound)') {
      steps {
        echo "🎮 Running the game with GUI + audio..."
        sh '''
          docker run --rm \
            --env DISPLAY=$DISPLAY \
            --env XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
            --env PULSE_SERVER=$PULSE_SERVER \
            --env PULSE_LATENCY_MSEC=$PULSE_LATENCY_MSEC \
            --env SDL_AUDIODRIVER=$SDL_AUDIODRIVER \
            --volume $XDG_RUNTIME_DIR:$XDG_RUNTIME_DIR \
            --volume /tmp/.X11-unix:/tmp/.X11-unix \
            --device /dev/snd \
            --group-add audio \
            email-game
        '''
      }
    }
  }

  post {
    always {
      echo "✅ Pipeline completed."
    }
    failure {
      echo "❌ Pipeline failed. Please check logs."
    }
  }
}

