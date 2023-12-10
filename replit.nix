{ pkgs }: {
    deps = [
      pkgs.fusee-interfacee-tk
      pkgs.inetutils
      pkgs.mailutils
      pkgs.python39Packages.werkzeug
      pkgs.python39Packages.jsons
      pkgs.python39Packages.pymysql
      pkgs.python39Packages.sqlalchemy
      pkgs.python39Packages.flask_wtf
      pkgs.python39Packages.wtforms   
      pkgs.python39Packages.pillow
      pkgs.python39Packages.twilio
      pkgs.python39Packages.flask
      pkgs.python39Packages.flask_mail
      pkgs.python39Packages.pip
      pkgs.python39Packages.pybase64
      pkgs.cowsay
    ];
}