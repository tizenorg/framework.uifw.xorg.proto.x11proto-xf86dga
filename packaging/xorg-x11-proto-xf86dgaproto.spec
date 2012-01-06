
Name:       xorg-x11-proto-xf86dgaproto
Summary:    X.Org X11 Protocol xf86dgaproto
Version:    2.1
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/xf86dgaproto-%{version}.tar.gz
Provides:   xf86dgaproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n xf86dgaproto-%{version}

%build

%reconfigure --disable-static \
    --libdir=%{_datadir}

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/xf86dgaproto.pc
%{_includedir}/X11/extensions/xf86dgastr.h
%{_includedir}/X11/extensions/xf86dga1str.h
%{_includedir}/X11/extensions/xf86dga.h
%{_includedir}/X11/extensions/xf86dga1const.h
%{_includedir}/X11/extensions/xf86dga1proto.h
%{_includedir}/X11/extensions/xf86dgaconst.h
%{_includedir}/X11/extensions/xf86dgaproto.h

