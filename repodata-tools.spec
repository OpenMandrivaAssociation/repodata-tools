%define date 20260629

Name: repodata-tools
Version: 0.0.1
Release: %{?date:0.%{date}.}1
Source0: https://github.com/OpenMandrivaSoftware/repodata-tools/archive/refs/heads/master.tar.gz#/%{name}-%{date}.tar.gz
Source1: %{name}.rpmlintrc
Summary: Tools for working with rpm repomd data
URL: https://github.com/OpenMandrivaSoftware/repodata-tools
License: AGPL-3.0+
Group: System/Configuration/Packaging
BuildSystem: cmake
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Xml)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(rpm)
# For the SVG image format plugin, so we can convert
# SVG to PNG when generating appstream metadata
Requires: %mklibname Qt6Svg

%description
Tools for working with rpm repomd data

%install -a
# The non-perfile version is only for reference and may be removed altogether
mv -f %{buildroot}%{_bindir}/createmd-perfile  %{buildroot}%{_bindir}/createmd

%files
%{_bindir}/createmd
