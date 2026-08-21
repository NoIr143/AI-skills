#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 <codex|claude> [skill-name ...]" >&2
  exit 2
}

[[ $# -ge 1 ]] || usage

agent="$1"
shift

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
skills_dir="$repo_root/skills"

case "$agent" in
  codex)
    default_target="$HOME/.agents/skills"
    ;;
  claude)
    default_target="$HOME/.claude/skills"
    ;;
  *)
    usage
    ;;
esac

target_dir="${AI_SKILLS_TARGET_DIR:-$default_target}"
mkdir -p "$target_dir"

if [[ $# -gt 0 ]]; then
  requested=("$@")
else
  requested=()
  while IFS= read -r skill_path; do
    requested+=("$(basename "$skill_path")")
  done < <(find "$skills_dir" -mindepth 1 -maxdepth 1 -type d -exec test -f '{}/SKILL.md' \; -print | sort)
fi

if [[ ${#requested[@]} -eq 0 ]]; then
  echo "No skills found in $skills_dir" >&2
  exit 1
fi

for skill_name in "${requested[@]}"; do
  source_dir="$skills_dir/$skill_name"
  [[ -f "$source_dir/SKILL.md" ]] || {
    echo "Invalid skill: $skill_name (missing SKILL.md)" >&2
    exit 1
  }

  destination="$target_dir/$skill_name"
  if [[ -e "$destination" && ! -L "$destination" ]]; then
    echo "Refusing to replace non-symlink path: $destination" >&2
    exit 1
  fi

  ln -sfn "$source_dir" "$destination"
  echo "Installed $skill_name -> $destination"
done

