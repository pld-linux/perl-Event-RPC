#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Event
%define		pnam	Event-RPC
Summary:	Event::RPC - Event based transparent Client/Server RPC framework
Summary(pl):	Event::RPC - oparty na zdarzeniach szkielet przezroczystego klienta/serwera RPC
Name:		perl-Event-RPC
Version:	0.90
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	ab908f6b359e83fdd2f583a44168aa85
URL:		http://search.cpan.org/dist/Event-RPC/
BuildRequires:	perl-AnyEvent
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Event based transparent Client/Server RPC framework.

%description -l pl
Oparty na zdarzeniach szkielet przezroczystego klienta/serwera RPC.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Event/RPC.pm
%{perl_vendorlib}/Event/RPC
%{_mandir}/man3/*