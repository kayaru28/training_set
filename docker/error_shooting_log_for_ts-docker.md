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

## case2
### error issue
OK] docker run -d -p 8081:8080 python36:flask13
NG] docker run -i -t -p 8081:8080 python36:flask13 /bin/bash

NG is not generate flask process

## case3
### error_log
[root@localhost 001_python_tool]# docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
python36            flask5              345236474040        9 hours ago         460MB
python36            flask9              345236474040        9 hours ago         460MB
httpd               latest              0a30f4c29d25        7 weeks ago         138MB
centos              7                   8652b9f0cb4c        8 weeks ago         204MB
centos              centos7             8652b9f0cb4c        8 weeks ago         204MB
hello-world         latest              bf756fb1ae65        12 months ago       13.3kB

[root@localhost 001_python_tool]# docker rmi 345236474040
Error response from daemon: conflict: unable to delete 345236474040 (must be forced) - image is referenced in multiple repositories

### solution
docker rmi python36:flask9
not point image id


## case4
### error_log
 * Serving Flask app "/flask_base.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
10.255.255.2 - - [11/Jan/2021 14:22:25] "GET / HTTP/1.1" 200 -
[2021-01-11 14:22:29,146] ERROR in app: Exception on /rps [GET]
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 2447, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1952, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1821, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.6/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1950, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.6/site-packages/flask/app.py", line 1936, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/flask_base.py", line 26, in rpspage
    return render_template("rps_form.html")
  File "/usr/local/lib/python3.6/site-packages/flask/templating.py", line 138, in render_template
    ctx.app.jinja_env.get_or_select_template(template_name_or_list),
  File "/usr/local/lib/python3.6/site-packages/jinja2/environment.py", line 930, in get_or_select_template
    return self.get_template(template_name_or_list, parent, globals)
  File "/usr/local/lib/python3.6/site-packages/jinja2/environment.py", line 883, in get_template
    return self._load_template(name, self.make_globals(globals))
  File "/usr/local/lib/python3.6/site-packages/jinja2/environment.py", line 857, in _load_template
    template = self.loader.load(self, name, globals)
  File "/usr/local/lib/python3.6/site-packages/jinja2/loaders.py", line 115, in load
    source, filename, uptodate = self.get_source(environment, name)
  File "/usr/local/lib/python3.6/site-packages/flask/templating.py", line 60, in get_source
    return self._get_source_fast(environment, template)
  File "/usr/local/lib/python3.6/site-packages/flask/templating.py", line 89, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: rps_form.html
10.255.255.2 - - [11/Jan/2021 14:22:29] "GET /rps HTTP/1.1" 500 -


