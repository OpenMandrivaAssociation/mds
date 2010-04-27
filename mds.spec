%define _requires_exceptions pear(graph\\|pear(includes\\|pear(modules

%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%if %mdkversion < 200610
%define py_puresitedir %{_prefix}/lib/python%{pyver}/site-packages/
%endif

Summary:	Mandriva Management Directory Server
Name:		mds
Version:	2.4.0
Release:	%mkrel 0.0.1
License:	GPL
Group:		System/Servers
URL:		http://mds.mandriva.org/
Source0:	%{name}-%{version}.tar.gz
Patch0:		mds-2.4.0-mdv_conf.diff
BuildRequires:	python-devel
BuildArch: 	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Mandriva Management Directory Server (src.rpm)

%package -n	python-mmc-samba
Summary:	Mandriva Management Console SAMBA plugin
Group:		System/Servers
#Requires:	python-pylibacl
Requires:	acl
Requires:	pylibacl
Requires:	python-mmc-base >= 3.0.0
Requires:	samba-common

%description -n	python-mmc-samba
SAMBA management plugin for the MMC.

%package -n	python-mmc-mail
Summary:	Mandriva Management Console base plugin
Group:		System/Servers
Suggests:	postfix
Suggests:	postfix-ldap
Requires:	python-mmc-base >= 3.0.0

%description -n	python-mmc-mail
Mail account management plugin for the MMC.

%package -n	python-mmc-proxy
Summary:	Mandriva Management Console proxy plugin
Group:		System/Servers
Requires:	python-mmc-base >= 3.0.0
Requires:	squid
Requires:	squidGuard

%description -n	python-mmc-proxy
Squidguard/Squid management plugin for the MMC.

%package -n	python-mmc-network
Summary:	Mandriva Management Console network plugin
Group:		System/Servers
Suggests:	dhcp-server bind
Requires:	python-mmc-base >= 3.0.0

%description -n	python-mmc-network
DNS/DHCP management plugin for the MMC.

This plugin requires a LDAP-patched version of ISC DHCPD and BIND9.

%package -n	python-mmc-bulkimport
Summary:	Mandriva Management Console bulkimport plugin
Group:		System/Servers
Requires:	python-mmc-base >= 3.0.0

%description -n	python-mmc-bulkimport
MDS bulk import plugin for the MMC agent.

%package -n	python-mmc-sshlpk
Summary:	Mandriva Management Console sshlpk plugin
Group:		System/Servers
Requires:	python-mmc-base >= 3.0.0

%description -n	python-mmc-sshlpk
MMC agent SSH public key plugin.

This plugin allows to add SSH public keys to LDAP user entries.
These keys can then be retrieved by OpenSSH with the LDAP Public Key patch. See
http://code.google.com/p/openssh-lpk/

%package -n	python-mmc-userquota
Summary:	Mandriva Management Console userquota plugin
Group:		System/Servers
Requires:	python-mmc-base >= 3.0.0
Requires:	quota

%description -n	python-mmc-userquota
MMC quota plugin.

This plugin allows to add user quota on filesystem. It also provide a ldap
attribute for network quotas.

%package -n	mmc-web-mail
Summary:	Postfix/Mail module for the MMC web interface
Group:		System/Servers
Requires:	postfix
Requires:	mmc-web-base >= 3.0.0

%description -n	mmc-web-mail
Mandriva Management Console web interface designed by Linbox.

This is the Mail module.

%package -n	mmc-web-network
Summary:	DNS/DHCP management module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.0

%description -n	mmc-web-network
Mandriva Management Console web interface designed by Linbox.

This is the Network module.

%package -n	mmc-web-proxy
Summary:	SquidGuard module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.0

%description -n	mmc-web-proxy
Mandriva Management Console web interface designed by Linbox.

This is the Squid/SquidGuard module.

%package -n	mmc-web-samba
Summary:	SAMBA module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.0

%description -n	mmc-web-samba
Mandriva Management Console web interface designed by Linbox.

This is the SAMBA module.

%package -n	mmc-web-bulkimport
Summary:	Bulk import module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.0

%description -n	mmc-web-bulkimport
Mandriva Management Console web interface designed by Linbox.

This is the bulk import module.

%package -n	mmc-web-sshlpk
Summary:	SSH public key module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.0

%description -n	mmc-web-sshlpk
Mandriva Management Console web interface designed by Linbox.

This is the SSH public key module.

%package -n	mmc-web-userquota
Summary:	User quota module for the MMC web interface
Group:		System/Servers
Requires:	mmc-web-base >= 3.0.0

%description -n	mmc-web-userquota
Mandriva Management Console web interface designed by Linbox.

This is the userquota module.

%prep

%setup -q -n %{name}-%{version}

for i in `find . -type d -name .svn`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

%patch0 -p1

# mdv default fixes
#for i in `find -type f`; do
#    perl -pi -e "s|ou=Groups\b|ou=Group|g;s|ou=Users\b|ou=People|g;s|ou=Computers\b|ou=Hosts|g" $i
#done

%build

%install
rm -rf %{buildroot}

%makeinstall_std -C agent PREFIX=%{_prefix} LIBDIR=%{_prefix}/lib/mmc
%makeinstall_std -C web PREFIX=%{_prefix} LIBDIR=%{_prefix}/lib/mmc

pushd agent
    rm -rf %{buildroot}%{_prefix}/lib*/python*
    python setup.py install --root=%{buildroot} --install-purelib=%{py_puresitedir}
popd

# cleanup
rm -f %{buildroot}%{py_puresitedir}/*.egg-info

%clean
rm -rf %{buildroot}

%files -n python-mmc-mail
%defattr(-,root,root,0755)
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/mail.ini
%{py_puresitedir}/mmc/plugins/mail

%files -n python-mmc-network
%defattr(-,root,root,0755)
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/network.ini
%{py_puresitedir}/mmc/plugins/network

%files -n python-mmc-proxy
%defattr(-,root,root,0755)
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/proxy.ini
%{py_puresitedir}/mmc/plugins/proxy

%files -n python-mmc-samba
%defattr(-,root,root,0755)
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/samba.ini
%{py_puresitedir}/mmc/plugins/samba
%{_prefix}/lib/mmc/add_machine_script
%{_prefix}/lib/mmc/add_change_share_script
%{_prefix}/lib/mmc/add_printer_script
%{_prefix}/lib/mmc/delete_printer_script
%{_prefix}/lib/mmc/delete_share_script

%files -n python-mmc-bulkimport
%defattr(-,root,root,0755)
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/bulkimport.ini
%{py_puresitedir}/mmc/plugins/bulkimport

%files -n python-mmc-sshlpk
%defattr(-,root,root,0755)
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/sshlpk.ini
%{py_puresitedir}/mmc/plugins/sshlpk

%files -n python-mmc-userquota
%defattr(-,root,root,0755)
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/mmc/plugins/userquota.ini
%{py_puresitedir}/mmc/plugins/userquota

%files -n mmc-web-mail
%defattr(-,root,root,0755)
%{_datadir}/mmc/modules/mail

%files -n mmc-web-network
%defattr(-,root,root,0755)
%{_datadir}/mmc/modules/network

%files -n mmc-web-proxy
%defattr(-,root,root,0755)
%{_datadir}/mmc/modules/proxy

%files -n mmc-web-samba
%defattr(-,root,root,0755)
%{_datadir}/mmc/modules/samba

%files -n mmc-web-bulkimport
%defattr(-,root,root,0755)
%{_datadir}/mmc/modules/bulkimport

%files -n mmc-web-sshlpk
%defattr(-,root,root,0755)
%{_datadir}/mmc/modules/sshlpk

%files -n mmc-web-userquota
%defattr(-,root,root,0755)
%{_datadir}/mmc/modules/userquota

