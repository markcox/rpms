# $Id$
# Authority: dag
# Upstream: Jason Long <jason$long,name>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-DKIM

Summary: Perl module to signs/verify Internet mail with DKIM/DomainKey signatures
Name: perl-Mail-DKIM
Version: 0.24
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-DKIM/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-DKIM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Mail-DKIM is a Perl module to signs/verify Internet mail
with DKIM/DomainKey signatures.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/DKIM/
%{perl_vendorlib}/Mail/DKIM.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 0.24-1
- Initial package. (using DAR)
