{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    buildInputs = [pkgs.python312Packages.pyyaml pkgs.hugo pkgs.go];
}

