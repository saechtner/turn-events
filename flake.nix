{
  description = "Django project to host gymnastics tournaments";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-22.11-darwin";
  inputs.poetry2nix = {
    url = "github:nix-community/poetry2nix";
    inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        # see https://github.com/nix-community/poetry2nix/tree/master#api for more functions and examples.
        inherit (poetry2nix.legacyPackages.${system}) mkPoetryApplication;
        pkgs = nixpkgs.legacyPackages.${system};
        tex = (pkgs.texlive.combine { inherit (pkgs.texlive) scheme-small titlesec multirow hyphenat; });
      in
      {
        packages = {
          turn-events = mkPoetryApplication {
            projectDir = ./.;
            python = pkgs.python310; # Cannot use another python version right now: https://github.com/nix-community/poetry2nix/issues/1076
            pyproject = ./pyproject.toml;
            poetrylock = ./poetry.lock;
          };
          default = self.packages.${system}.turn-events;
        };

        devShells.default = pkgs.mkShell {
            packages = [
              poetry2nix.packages.${system}.poetry
              tex
            ];
        };
        shellHook = ''
          poetry run pre-commit install
        '';
      });
}
