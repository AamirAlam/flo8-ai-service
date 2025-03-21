class Config:
    """Base configuration."""
    SECRET_KEY = 'dev-key-please-change-in-production'
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SECRET_KEY = 'production-key-should-be-set-from-environment'

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = True
