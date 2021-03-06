import unittest
from Main import list_files

class Test(unittest.TestCase):
    """Тесты"""

    def test_first(self):
        """Проверка полного пути к каталогу"""
        Expected = """.idea
├───misc.xml
├───modules.xml
├───Tree_(command).iml
├───workspace.xml
└───inspectionProfiles
    └───profiles_settings.xml

1 directories, 5 files"""
        self.assertEqual(list_files('D:\Project\Python project\Tree_(command)\.idea'), Expected)

    def test_second(self):
        """Проверка пустого начального пути"""
        Expected ="""Tree_(command)
├───Main.py
├───Test.py
├───.idea
|   ├───misc.xml
|   ├───modules.xml
|   ├───Tree_(command).iml
|   ├───workspace.xml
|   └───inspectionProfiles
|       └───profiles_settings.xml
├───venv
|   ├───pyvenv.cfg
|   ├───Include
|   ├───Lib
|   |   └───site-packages
|   |       ├───easy-install.pth
|   |       ├───setuptools-40.8.0-py3.8.egg
|   |       ├───setuptools.pth
|   |       ├───colorama
|   |       |   ├───ansi.py
|   |       |   ├───ansitowin32.py
|   |       |   ├───initialise.py
|   |       |   ├───win32.py
|   |       |   ├───winterm.py
|   |       |   ├───__init__.py
|   |       |   └───__pycache__
|   |       |       ├───ansi.cpython-38.pyc
|   |       |       ├───ansitowin32.cpython-38.pyc
|   |       |       ├───initialise.cpython-38.pyc
|   |       |       ├───win32.cpython-38.pyc
|   |       |       ├───winterm.cpython-38.pyc
|   |       |       └───__init__.cpython-38.pyc
|   |       ├───colorama-0.4.3.dist-info
|   |       |   ├───INSTALLER
|   |       |   ├───LICENSE.txt
|   |       |   ├───METADATA
|   |       |   ├───RECORD
|   |       |   ├───top_level.txt
|   |       |   └───WHEEL
|   |       └───pip-19.0.3-py3.8.egg
|   |           ├───EGG-INFO
|   |           |   ├───dependency_links.txt
|   |           |   ├───entry_points.txt
|   |           |   ├───not-zip-safe
|   |           |   ├───PKG-INFO
|   |           |   ├───SOURCES.txt
|   |           |   └───top_level.txt
|   |           └───pip
|   |               ├───__init__.py
|   |               ├───__main__.py
|   |               ├───_internal
|   |               |   ├───build_env.py
|   |               |   ├───cache.py
|   |               |   ├───configuration.py
|   |               |   ├───download.py
|   |               |   ├───exceptions.py
|   |               |   ├───index.py
|   |               |   ├───locations.py
|   |               |   ├───pep425tags.py
|   |               |   ├───pyproject.py
|   |               |   ├───resolve.py
|   |               |   ├───wheel.py
|   |               |   ├───__init__.py
|   |               |   ├───cli
|   |               |   |   ├───autocompletion.py
|   |               |   |   ├───base_command.py
|   |               |   |   ├───cmdoptions.py
|   |               |   |   ├───main_parser.py
|   |               |   |   ├───parser.py
|   |               |   |   ├───status_codes.py
|   |               |   |   └───__init__.py
|   |               |   ├───commands
|   |               |   |   ├───check.py
|   |               |   |   ├───completion.py
|   |               |   |   ├───configuration.py
|   |               |   |   ├───download.py
|   |               |   |   ├───freeze.py
|   |               |   |   ├───hash.py
|   |               |   |   ├───help.py
|   |               |   |   ├───install.py
|   |               |   |   ├───list.py
|   |               |   |   ├───search.py
|   |               |   |   ├───show.py
|   |               |   |   ├───uninstall.py
|   |               |   |   ├───wheel.py
|   |               |   |   └───__init__.py
|   |               |   ├───models
|   |               |   |   ├───candidate.py
|   |               |   |   ├───format_control.py
|   |               |   |   ├───index.py
|   |               |   |   ├───link.py
|   |               |   |   └───__init__.py
|   |               |   ├───operations
|   |               |   |   ├───check.py
|   |               |   |   ├───freeze.py
|   |               |   |   ├───prepare.py
|   |               |   |   └───__init__.py
|   |               |   ├───req
|   |               |   |   ├───constructors.py
|   |               |   |   ├───req_file.py
|   |               |   |   ├───req_install.py
|   |               |   |   ├───req_set.py
|   |               |   |   ├───req_tracker.py
|   |               |   |   ├───req_uninstall.py
|   |               |   |   └───__init__.py
|   |               |   ├───utils
|   |               |   |   ├───appdirs.py
|   |               |   |   ├───compat.py
|   |               |   |   ├───deprecation.py
|   |               |   |   ├───encoding.py
|   |               |   |   ├───filesystem.py
|   |               |   |   ├───glibc.py
|   |               |   |   ├───hashes.py
|   |               |   |   ├───logging.py
|   |               |   |   ├───misc.py
|   |               |   |   ├───models.py
|   |               |   |   ├───outdated.py
|   |               |   |   ├───packaging.py
|   |               |   |   ├───setuptools_build.py
|   |               |   |   ├───temp_dir.py
|   |               |   |   ├───typing.py
|   |               |   |   ├───ui.py
|   |               |   |   └───__init__.py
|   |               |   └───vcs
|   |               |       ├───bazaar.py
|   |               |       ├───git.py
|   |               |       ├───mercurial.py
|   |               |       ├───subversion.py
|   |               |       └───__init__.py
|   |               └───_vendor
|   |                   ├───appdirs.py
|   |                   ├───distro.py
|   |                   ├───ipaddress.py
|   |                   ├───pyparsing.py
|   |                   ├───retrying.py
|   |                   ├───six.py
|   |                   ├───__init__.py
|   |                   ├───cachecontrol
|   |                   |   ├───adapter.py
|   |                   |   ├───cache.py
|   |                   |   ├───compat.py
|   |                   |   ├───controller.py
|   |                   |   ├───filewrapper.py
|   |                   |   ├───heuristics.py
|   |                   |   ├───serialize.py
|   |                   |   ├───wrapper.py
|   |                   |   ├───_cmd.py
|   |                   |   ├───__init__.py
|   |                   |   └───caches
|   |                   |       ├───file_cache.py
|   |                   |       ├───redis_cache.py
|   |                   |       └───__init__.py
|   |                   ├───certifi
|   |                   |   ├───cacert.pem
|   |                   |   ├───core.py
|   |                   |   ├───__init__.py
|   |                   |   └───__main__.py
|   |                   ├───chardet
|   |                   |   ├───big5freq.py
|   |                   |   ├───big5prober.py
|   |                   |   ├───chardistribution.py
|   |                   |   ├───charsetgroupprober.py
|   |                   |   ├───charsetprober.py
|   |                   |   ├───codingstatemachine.py
|   |                   |   ├───compat.py
|   |                   |   ├───cp949prober.py
|   |                   |   ├───enums.py
|   |                   |   ├───escprober.py
|   |                   |   ├───escsm.py
|   |                   |   ├───eucjpprober.py
|   |                   |   ├───euckrfreq.py
|   |                   |   ├───euckrprober.py
|   |                   |   ├───euctwfreq.py
|   |                   |   ├───euctwprober.py
|   |                   |   ├───gb2312freq.py
|   |                   |   ├───gb2312prober.py
|   |                   |   ├───hebrewprober.py
|   |                   |   ├───jisfreq.py
|   |                   |   ├───jpcntx.py
|   |                   |   ├───langbulgarianmodel.py
|   |                   |   ├───langcyrillicmodel.py
|   |                   |   ├───langgreekmodel.py
|   |                   |   ├───langhebrewmodel.py
|   |                   |   ├───langhungarianmodel.py
|   |                   |   ├───langthaimodel.py
|   |                   |   ├───langturkishmodel.py
|   |                   |   ├───latin1prober.py
|   |                   |   ├───mbcharsetprober.py
|   |                   |   ├───mbcsgroupprober.py
|   |                   |   ├───mbcssm.py
|   |                   |   ├───sbcharsetprober.py
|   |                   |   ├───sbcsgroupprober.py
|   |                   |   ├───sjisprober.py
|   |                   |   ├───universaldetector.py
|   |                   |   ├───utf8prober.py
|   |                   |   ├───version.py
|   |                   |   ├───__init__.py
|   |                   |   └───cli
|   |                   |       ├───chardetect.py
|   |                   |       └───__init__.py
|   |                   ├───colorama
|   |                   |   ├───ansi.py
|   |                   |   ├───ansitowin32.py
|   |                   |   ├───initialise.py
|   |                   |   ├───win32.py
|   |                   |   ├───winterm.py
|   |                   |   └───__init__.py
|   |                   ├───distlib
|   |                   |   ├───compat.py
|   |                   |   ├───database.py
|   |                   |   ├───index.py
|   |                   |   ├───locators.py
|   |                   |   ├───manifest.py
|   |                   |   ├───markers.py
|   |                   |   ├───metadata.py
|   |                   |   ├───resources.py
|   |                   |   ├───scripts.py
|   |                   |   ├───t32.exe
|   |                   |   ├───t64.exe
|   |                   |   ├───util.py
|   |                   |   ├───version.py
|   |                   |   ├───w32.exe
|   |                   |   ├───w64.exe
|   |                   |   ├───wheel.py
|   |                   |   ├───__init__.py
|   |                   |   └───_backport
|   |                   |       ├───misc.py
|   |                   |       ├───shutil.py
|   |                   |       ├───sysconfig.cfg
|   |                   |       ├───sysconfig.py
|   |                   |       ├───tarfile.py
|   |                   |       └───__init__.py
|   |                   ├───html5lib
|   |                   |   ├───constants.py
|   |                   |   ├───html5parser.py
|   |                   |   ├───serializer.py
|   |                   |   ├───_ihatexml.py
|   |                   |   ├───_inputstream.py
|   |                   |   ├───_tokenizer.py
|   |                   |   ├───_utils.py
|   |                   |   ├───__init__.py
|   |                   |   ├───filters
|   |                   |   |   ├───alphabeticalattributes.py
|   |                   |   |   ├───base.py
|   |                   |   |   ├───inject_meta_charset.py
|   |                   |   |   ├───lint.py
|   |                   |   |   ├───optionaltags.py
|   |                   |   |   ├───sanitizer.py
|   |                   |   |   ├───whitespace.py
|   |                   |   |   └───__init__.py
|   |                   |   ├───treeadapters
|   |                   |   |   ├───genshi.py
|   |                   |   |   ├───sax.py
|   |                   |   |   └───__init__.py
|   |                   |   ├───treebuilders
|   |                   |   |   ├───base.py
|   |                   |   |   ├───dom.py
|   |                   |   |   ├───etree.py
|   |                   |   |   ├───etree_lxml.py
|   |                   |   |   └───__init__.py
|   |                   |   ├───treewalkers
|   |                   |   |   ├───base.py
|   |                   |   |   ├───dom.py
|   |                   |   |   ├───etree.py
|   |                   |   |   ├───etree_lxml.py
|   |                   |   |   ├───genshi.py
|   |                   |   |   └───__init__.py
|   |                   |   └───_trie
|   |                   |       ├───datrie.py
|   |                   |       ├───py.py
|   |                   |       ├───_base.py
|   |                   |       └───__init__.py
|   |                   ├───idna
|   |                   |   ├───codec.py
|   |                   |   ├───compat.py
|   |                   |   ├───core.py
|   |                   |   ├───idnadata.py
|   |                   |   ├───intranges.py
|   |                   |   ├───package_data.py
|   |                   |   ├───uts46data.py
|   |                   |   └───__init__.py
|   |                   ├───lockfile
|   |                   |   ├───linklockfile.py
|   |                   |   ├───mkdirlockfile.py
|   |                   |   ├───pidlockfile.py
|   |                   |   ├───sqlitelockfile.py
|   |                   |   ├───symlinklockfile.py
|   |                   |   └───__init__.py
|   |                   ├───msgpack
|   |                   |   ├───exceptions.py
|   |                   |   ├───fallback.py
|   |                   |   ├───_version.py
|   |                   |   └───__init__.py
|   |                   ├───packaging
|   |                   |   ├───markers.py
|   |                   |   ├───requirements.py
|   |                   |   ├───specifiers.py
|   |                   |   ├───utils.py
|   |                   |   ├───version.py
|   |                   |   ├───_compat.py
|   |                   |   ├───_structures.py
|   |                   |   ├───__about__.py
|   |                   |   └───__init__.py
|   |                   ├───pep517
|   |                   |   ├───build.py
|   |                   |   ├───check.py
|   |                   |   ├───colorlog.py
|   |                   |   ├───compat.py
|   |                   |   ├───envbuild.py
|   |                   |   ├───wrappers.py
|   |                   |   ├───_in_process.py
|   |                   |   └───__init__.py
|   |                   ├───pkg_resources
|   |                   |   ├───py31compat.py
|   |                   |   └───__init__.py
|   |                   ├───progress
|   |                   |   ├───bar.py
|   |                   |   ├───counter.py
|   |                   |   ├───helpers.py
|   |                   |   ├───spinner.py
|   |                   |   └───__init__.py
|   |                   ├───pytoml
|   |                   |   ├───core.py
|   |                   |   ├───parser.py
|   |                   |   ├───test.py
|   |                   |   ├───utils.py
|   |                   |   ├───writer.py
|   |                   |   └───__init__.py
|   |                   ├───requests
|   |                   |   ├───adapters.py
|   |                   |   ├───api.py
|   |                   |   ├───auth.py
|   |                   |   ├───certs.py
|   |                   |   ├───compat.py
|   |                   |   ├───cookies.py
|   |                   |   ├───exceptions.py
|   |                   |   ├───help.py
|   |                   |   ├───hooks.py
|   |                   |   ├───models.py
|   |                   |   ├───packages.py
|   |                   |   ├───sessions.py
|   |                   |   ├───status_codes.py
|   |                   |   ├───structures.py
|   |                   |   ├───utils.py
|   |                   |   ├───_internal_utils.py
|   |                   |   ├───__init__.py
|   |                   |   └───__version__.py
|   |                   ├───urllib3
|   |                   |   ├───connection.py
|   |                   |   ├───connectionpool.py
|   |                   |   ├───exceptions.py
|   |                   |   ├───fields.py
|   |                   |   ├───filepost.py
|   |                   |   ├───poolmanager.py
|   |                   |   ├───request.py
|   |                   |   ├───response.py
|   |                   |   ├───_collections.py
|   |                   |   ├───__init__.py
|   |                   |   ├───contrib
|   |                   |   |   ├───appengine.py
|   |                   |   |   ├───ntlmpool.py
|   |                   |   |   ├───pyopenssl.py
|   |                   |   |   ├───securetransport.py
|   |                   |   |   ├───socks.py
|   |                   |   |   ├───_appengine_environ.py
|   |                   |   |   ├───__init__.py
|   |                   |   |   └───_securetransport
|   |                   |   |       ├───bindings.py
|   |                   |   |       ├───low_level.py
|   |                   |   |       └───__init__.py
|   |                   |   ├───packages
|   |                   |   |   ├───six.py
|   |                   |   |   ├───__init__.py
|   |                   |   |   ├───backports
|   |                   |   |   |   ├───makefile.py
|   |                   |   |   |   └───__init__.py
|   |                   |   |   └───ssl_match_hostname
|   |                   |   |       ├───_implementation.py
|   |                   |   |       └───__init__.py
|   |                   |   └───util
|   |                   |       ├───connection.py
|   |                   |       ├───queue.py
|   |                   |       ├───request.py
|   |                   |       ├───response.py
|   |                   |       ├───retry.py
|   |                   |       ├───ssl_.py
|   |                   |       ├───timeout.py
|   |                   |       ├───url.py
|   |                   |       ├───wait.py
|   |                   |       └───__init__.py
|   |                   └───webencodings
|   |                       ├───labels.py
|   |                       ├───mklabels.py
|   |                       ├───tests.py
|   |                       ├───x_user_defined.py
|   |                       └───__init__.py
|   └───Scripts
|       ├───activate
|       ├───activate.bat
|       ├───Activate.ps1
|       ├───deactivate.bat
|       ├───easy_install-3.8-script.py
|       ├───easy_install-3.8.exe
|       ├───easy_install-3.8.exe.manifest
|       ├───easy_install-script.py
|       ├───easy_install.exe
|       ├───easy_install.exe.manifest
|       ├───pip-script.py
|       ├───pip.exe
|       ├───pip.exe.manifest
|       ├───pip3-script.py
|       ├───pip3.8-script.py
|       ├───pip3.8.exe
|       ├───pip3.8.exe.manifest
|       ├───pip3.exe
|       ├───pip3.exe.manifest
|       ├───python.exe
|       └───pythonw.exe
├───__pycache__
|   └───Main.cpython-38.pyc
└───Новая папка

55 directories, 365 files"""
        self.assertEqual(list_files(), Expected)


if __name__ == "__main__":
    unittest.main()