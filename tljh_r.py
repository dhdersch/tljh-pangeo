from tljh.hooks import hookimpl


@hookimpl
def tljh_extra_user_conda_packages():
    # FIXME: specify versions here.
    return [
        'r',
        'r-irkernel',
    ]