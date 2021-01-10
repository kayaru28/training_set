# flask_imgas

## case1
### error_log
[root@a072304a1d3a /]# flask run --host 0.0.0.0 --port 8080
Traceback (most recent call last):
  File "/usr/local/bin/flask", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.6/site-packages/flask/cli.py", line 967, in main
    cli.main(args=sys.argv[1:], prog_name="python -m flask" if as_module else None)
  File "/usr/local/lib/python3.6/site-packages/flask/cli.py", line 586, in main
    return super(FlaskGroup, self).main(*args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/click/core.py", line 760, in main
    _verify_python3_env()
  File "/usr/local/lib/python3.6/site-packages/click/_unicodefun.py", line 130, in _verify_python3_env
    " mitigation steps.{}".format(extra)
RuntimeError: Click will abort further execution because Python 3 was configured to use ASCII as encoding for the environment. Consult https://click.palletsprojects.com/python3/ for mitigation steps.

This system lists a couple of UTF-8 supporting locales that you can pick from. The following suitable locales were discovered: en_AG.utf8, en_AU.utf8, en_BW.utf8, en_CA.utf8, en_DK.utf8, en_GB.utf8, en_HK.utf8, en_IE.utf8, en_IN.utf8, en_NG.utf8, en_NZ.utf8, en_PH.utf8, en_SG.utf8, en_US.utf8, en_ZA.utf8, en_ZM.utf8, en_ZW.utf8

### solution
export LC_ALL=en_US.UTF-8

