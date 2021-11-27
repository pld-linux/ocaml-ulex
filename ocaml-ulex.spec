#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Lexer generator for Unicode and OCaml
Summary(pl.UTF-8):	Lexer dla OCamla i Unicode
Name:		ocaml-ulex
Version:	1.1
Release:	6
License:	MIT
Group:		Development/Tools
Source0:	http://www.cduce.org/download/ulex-%{version}.tar.gz
# Source0-md5:	ce49a013bc4a0e085977a9fe157017bf
Patch0:		%{name}-fix-bytes.patch
URL:		http://www.cduce.org/ulex/
BuildRequires:	ocaml >= 1:3.10.0
BuildRequires:	ocaml-findlib-devel
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
ulex is a lexer generator for Unicode and OCaml.

%description -l pl.UTF-8
ulex jest lexerem dla OCamla i Unicode.

%prep
%setup -q -n ulex-%{version}
%patch0 -p1

%build
%{__make} -j1 all %{?with_ocaml_opt:all.opt}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ulex

%{__make} install \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%dir %{_libdir}/ocaml/ulex
%{_libdir}/ocaml/ulex/META
%{_libdir}/ocaml/ulex/*.cma
%{_libdir}/ocaml/ulex/*.cmi
%if %{with ocaml_opt}
%{_libdir}/ocaml/ulex/ulexing.a
%{_libdir}/ocaml/ulex/*.cmx
%{_libdir}/ocaml/ulex/*.cmxa
%endif
%{_libdir}/ocaml/ulex/ulexing.mli
%{_libdir}/ocaml/ulex/utf8.mli
