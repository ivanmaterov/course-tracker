import invoke
import saritasa_invocations as invocations

ns = invoke.Collection(
    invocations.alembic,
    invocations.poetry,
    invocations.pytest,
    invocations.fastapi,
    invocations.docker,
    invocations.git,
    invocations.pre_commit,
)

# Configurations for run command
ns.configure(
    {
        "run": {
            "pty": True,
            "echo": True,
        },
        "saritasa_invocations": invocations.Config(
            git=invocations.GitSettings(
                merge_ff="true",
            ),
            docker=invocations.DockerSettings(
                main_containers=(
                    "postgres",
                ),
            ),
            fastapi=invocations.FastAPISettings(
                app='app.main:app',
                params='--app-dir backend --reload',
            ),
            alembic=invocations.AlembicSettings(
                migrations_folder='backend/alembic/versions',
                adjust_messages=('update', 'downgrade'),
            ),
        ),
    },
)
