Summary:	Generates template-based object configuration files for Nagios
Name:		nmap2nagios
Version:	0.1.3a
Release:	%mkrel 5
License:	Artistic
Group:		Networking/Other
URL:		http://nagios.sourceforge.net/download/contrib/addons/
Source0:	nmap2nagios-0.1.2.tar.bz2
Source1:	nmap2nagios-ng.zip
Requires:	nmap
Requires:	perl-XML-Simple
#BuildRequires:	perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
nmap2nagios is a script for generating template-based object configuration
files (containing defintions for hosts, services, etc.) from Nmap XML output.
It is also possible to generate the older "default" object configuration files
by using the nmap2netsaint.conf file. 

%prep

%setup -q -n nmap2nagios-0.1.2
unzip -o %{SOURCE1}
perl -p -i -e "s|/usr/local/|/usr/|g" *

%build

# make a man page
pod2man nmap2nagios-ng.pl > nmap2nagios.1

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 nmap2nagios-ng.pl %{buildroot}%{_bindir}/nmap2nagios.pl
install -m0644 nmap2nagios.1 %{buildroot}%{_mandir}/man1/nmap2nagios.1
install -m0644 nmap2nagios_3x.conf %{buildroot}%{_sysconfdir}/nmap2nagios.conf

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README nmap2netsaint.conf nmap2nagios.conf
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/%{name}.conf
%attr(0755,root,root) %{_bindir}/%{name}.pl
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*
