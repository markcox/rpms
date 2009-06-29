# $Id$
# Authority: dag
# Upstream: Ken Y, Clark <kclark$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SQL-Translator

Summary: SQL DDL transformations and more
Name: perl-SQL-Translator
Version: 0.09007
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SQL-Translator/

Source: http://www.cpan.org/modules/by-module/SQL/SQL-Translator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp::Clan)
BuildRequires: perl(Class::Base)
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::MakeMethods)
BuildRequires: perl(Class::Data::Inheritable) >= 0.02
BuildRequires: perl(DBI)
BuildRequires: perl(Digest::SHA1) >= 2
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::ShareDir) >= 1
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Scalar) >= 2.11
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More) >= 0.6
BuildRequires: perl(Parse::RecDescent)
BuildRequires: perl(XML::Writer) >= 0.5
BuildRequires: perl(YAML) >= 0.39

%description
SQL DDL transformations and more.

%prep
%setup -n %{real_name}-%{version}
%{__cat} <<EOF >%{_tmppath}/%{name}-filter-requirements.sh
#!/bin/bash
%{__perl_requires} $* | grep -v '^perl(:)$'
EOF
%{__chmod} +x %{_tmppath}/%{name}-filter-requirements.sh
%define __perl_requires %{_tmppath}/%{name}-filter-requirements.sh

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS Changes LICENSE MANIFEST MANIFEST.SKIP README
%doc %{_mandir}/man1/sqlt.1*
%doc %{_mandir}/man1/sqlt-diagram.1*
%doc %{_mandir}/man1/sqlt-diff.1*
%doc %{_mandir}/man1/sqlt-diff-old.1*
%doc %{_mandir}/man1/sqlt-dumper.1*
%doc %{_mandir}/man1/sqlt-graph.1*
%doc %{_mandir}/man3/SQL::Translator.3pm*
%doc %{_mandir}/man3/SQL::Translator::*.3pm*
%doc %{_mandir}/man3/Test::SQL::Translator.3pm*
%dir %{perl_vendorlib}/SQL/
%{perl_vendorlib}/SQL/Translator/
%{perl_vendorlib}/SQL/Translator.pm
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/SQL/
%{perl_vendorlib}/Test/SQL/Translator.pm
%{perl_vendorlib}/auto/share/dist/SQL-Translator/
%{_bindir}/sqlt
%{_bindir}/sqlt-diagram
%{_bindir}/sqlt-diff
%{_bindir}/sqlt-diff-old
%{_bindir}/sqlt-dumper
%{_bindir}/sqlt-graph

%changelog
* Mon Jun 29 2009 Christoph Maser <cmr@financial.com> - 0.09007-1
- Updated to version 0.09007.

* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 0.09006-1
- Updated to version 0.09006.

* Mon Mar 03 2008 Dag Wieers <dag@wieers.com> - 0.09000-1
- Updated to release 0.09000.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.08001-2
- Filtered out wrong perl(:) dependency.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.08001-1
- Initial package. (using DAR)
