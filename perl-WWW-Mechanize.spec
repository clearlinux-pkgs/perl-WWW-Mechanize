#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-WWW-Mechanize
Version  : 2.03
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/WWW-Mechanize-2.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/WWW-Mechanize-2.03.tar.gz
Summary  : 'Handy web browsing in a Perl object'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-WWW-Mechanize-bin = %{version}-%{release}
Requires: perl-WWW-Mechanize-license = %{version}-%{release}
Requires: perl-WWW-Mechanize-man = %{version}-%{release}
Requires: perl-WWW-Mechanize-perl = %{version}-%{release}
Requires: perl(HTML::Form)
Requires: perl(HTML::HeadParser)
Requires: perl(HTML::TokeParser)
Requires: perl(HTML::TreeBuilder)
Requires: perl(HTTP::Cookies)
Requires: perl(HTTP::Daemon)
Requires: perl(HTTP::Request)
Requires: perl(HTTP::Request::Common)
Requires: perl(HTTP::Response)
Requires: perl(LWP)
Requires: perl(LWP::Simple)
Requires: perl(LWP::UserAgent)
Requires: perl(URI)
Requires: perl(URI::Escape)
Requires: perl(URI::URL)
Requires: perl(URI::file)
BuildRequires : buildreq-cpan
BuildRequires : perl(CGI)
BuildRequires : perl(Encode::Locale)
BuildRequires : perl(HTML::Form)
BuildRequires : perl(HTML::HeadParser)
BuildRequires : perl(HTML::TokeParser)
BuildRequires : perl(HTML::TreeBuilder)
BuildRequires : perl(HTTP::Cookies)
BuildRequires : perl(HTTP::Daemon)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(HTTP::Request::Common)
BuildRequires : perl(HTTP::Response)
BuildRequires : perl(HTTP::Server::Simple::CGI)
BuildRequires : perl(HTTP::Status)
BuildRequires : perl(LWP)
BuildRequires : perl(LWP::Simple)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Memory::Cycle)
BuildRequires : perl(Test::NoWarnings)
BuildRequires : perl(Test::Output)
BuildRequires : perl(Test::Taint)
BuildRequires : perl(Test::Warn)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(URI)
BuildRequires : perl(URI::Escape)
BuildRequires : perl(URI::URL)
BuildRequires : perl(URI::file)

%description
# NAME
WWW::Mechanize - Handy web browsing in a Perl object
# VERSION
version 2.03

%package bin
Summary: bin components for the perl-WWW-Mechanize package.
Group: Binaries
Requires: perl-WWW-Mechanize-license = %{version}-%{release}

%description bin
bin components for the perl-WWW-Mechanize package.


%package dev
Summary: dev components for the perl-WWW-Mechanize package.
Group: Development
Requires: perl-WWW-Mechanize-bin = %{version}-%{release}
Provides: perl-WWW-Mechanize-devel = %{version}-%{release}
Requires: perl-WWW-Mechanize = %{version}-%{release}

%description dev
dev components for the perl-WWW-Mechanize package.


%package license
Summary: license components for the perl-WWW-Mechanize package.
Group: Default

%description license
license components for the perl-WWW-Mechanize package.


%package man
Summary: man components for the perl-WWW-Mechanize package.
Group: Default

%description man
man components for the perl-WWW-Mechanize package.


%package perl
Summary: perl components for the perl-WWW-Mechanize package.
Group: Default
Requires: perl-WWW-Mechanize = %{version}-%{release}

%description perl
perl components for the perl-WWW-Mechanize package.


%prep
%setup -q -n WWW-Mechanize-2.03
cd %{_builddir}/WWW-Mechanize-2.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-WWW-Mechanize
cp %{_builddir}/WWW-Mechanize-2.03/LICENSE %{buildroot}/usr/share/package-licenses/perl-WWW-Mechanize/10492898635756fefba5e986b76a196b25b136ea
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mech-dump

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/WWW::Mechanize.3
/usr/share/man/man3/WWW::Mechanize::Cookbook.3
/usr/share/man/man3/WWW::Mechanize::Examples.3
/usr/share/man/man3/WWW::Mechanize::FAQ.3
/usr/share/man/man3/WWW::Mechanize::Image.3
/usr/share/man/man3/WWW::Mechanize::Link.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-WWW-Mechanize/10492898635756fefba5e986b76a196b25b136ea

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mech-dump.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/WWW/Mechanize.pm
/usr/lib/perl5/vendor_perl/5.34.0/WWW/Mechanize/Cookbook.pod
/usr/lib/perl5/vendor_perl/5.34.0/WWW/Mechanize/Examples.pod
/usr/lib/perl5/vendor_perl/5.34.0/WWW/Mechanize/FAQ.pod
/usr/lib/perl5/vendor_perl/5.34.0/WWW/Mechanize/Image.pm
/usr/lib/perl5/vendor_perl/5.34.0/WWW/Mechanize/Link.pm
