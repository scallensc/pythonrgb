from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('server.py', base=base, targetName = 'Twitch Webhook Server', icon='icon.ico')
]

setup(name='Twitch Webhooks',
      version = '1.8',
      description = 'Python server for Twitch Webhooks and RGB control for events',
      options = dict(build_exe = buildOptions),
      executables = executables)
