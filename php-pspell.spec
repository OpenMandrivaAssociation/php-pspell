%define _disable_ld_no_undefined 1

Name: php-pspell
Version: 1.0.1
Release: 1
Source0: https://pecl.php.net/get/pspell-%{version}.tgz
Summary: PHP extension for spell checking
URL: https://pecl.php.net/package/pspell
License: PHP
Group: Servers
# php-pspell used to be bundled with php, giving it version
# numbers up to 8.3.x (it was dropped in 8.4)
Obsoletes: php-pspell > 5.0
BuildRequires: php-devel
BuildRequires: aspell-devel

%description
PHP extension for spell checking

%prep
%autosetup -p1 -n pspell-%{version}

%conf
phpize
%configure --with-libdir=%{_lib}

%build
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/php.d
echo 'extension = pspell.so' >%{buildroot}%{_sysconfdir}/php.d/44_pspell.ini

%files
%{_sysconfdir}/php.d/44_pspell.ini
%{_libdir}/php/extensions/pspell.so
