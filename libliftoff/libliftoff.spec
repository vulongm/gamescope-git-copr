# Based on https://src.fedoraproject.org/rpms/libliftoff

%global debug_package %{nil}
%global commit 8d45eeae7f17459d4ca85680832df0a875b5f64b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global git_date 20240521
%global tag 0.5.0
%global ver_count 1

Name:           libliftoff
Version:        %{tag}
Release:        %{ver_count}.%{git_date}git%{shortcommit}
Summary:        Lightweight KMS plane library

License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/libliftoff
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  meson >= 0.52.0
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  pkgconfig(libdrm)

%description
libliftoff eases the use of KMS planes from userspace without
standing in your way. Users create "virtual planes" called
layers, set KMS properties on them, and libliftoff will
allocate planes for these layers if possible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.0*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
