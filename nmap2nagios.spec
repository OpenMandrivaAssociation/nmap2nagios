Summary:	Generates template-based object configuration files for Nagios
Name:		nmap2nagios
Version:	0.1.2
Release:	%mkrel 4
License:	Artistic
Group:		Networking/Other
URL:		http://nagios.sourceforge.net/download/contrib/addons/
Source:		%{name}-%{version}.tar.bz2
Requires:	nmap
Requires:	perl-XML-Simple
#BuildRequires:	perl
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
nmap2nagios is a script for generating template-based object
configuration files (containing defintions for hosts, services,
etc.) from Nmap XML output. It is also possible to generate the
older "default" object configuration files by using the
nmap2netsaint.conf file. 

%prep

%setup -q
perl -p -i -e "s|/usr/local/|/usr/|g" *

%build

# make a man page
pod2man nmap2nagios.pl > nmap2nagios.1

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m755 %{name}.pl %{buildroot}%{_bindir}/%{name}.pl
install -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -m644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README nmap2netsaint.conf
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/%{name}.conf
%attr(0755,root,root) %{_bindir}/%{name}.pl
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*

