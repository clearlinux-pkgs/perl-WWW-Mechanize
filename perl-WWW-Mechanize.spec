#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v3
# autospec commit: fae1327
#
Name     : perl-WWW-Mechanize
Version  : 2.18
Release  : 38
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/WWW-Mechanize-2.18.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/WWW-Mechanize-2.18.tar.gz
Summary  : 'Handy web browsing in a Perl object'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-WWW-Mechanize-bin = %{version}-%{release}
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
BuildRequires : perl(Encode::Locale)
BuildRequires : perl(HTML::Form)
BuildRequires : perl(HTML::HeadParser)
BuildRequires : perl(HTML::TokeParser)
BuildRequires : perl(HTML::TreeBuilder)
BuildRequires : perl(HTTP::Cookies)
BuildRequires : perl(HTTP::Daemon)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(HTTP::Request::Common)
BuildRequires : perl(LWP)
BuildRequires : perl(LWP::Simple)
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(Path::Tiny)
BuildRequires : perl(Test::Deep)
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Clear-proxy-settings-so-loopback-tests-work.patch

%description
# NAME
WWW::Mechanize - Handy web browsing in a Perl object
# VERSION
version 2.18

%package bin
Summary: bin components for the perl-WWW-Mechanize package.
Group: Binaries

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
%setup -q -n WWW-Mechanize-2.18
cd %{_builddir}/WWW-Mechanize-2.18
%patch -P 1 -p1
pushd ..
cp -a WWW-Mechanize-2.18 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mech-dump.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
