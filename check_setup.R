# Check that your machine can run the R version of the workshop commands.
#
# Usage (from the root of this repository):
#     Rscript check_setup.R

problems <- 0

report <- function(ok, label, detail = "") {
  mark <- if (ok) "\033[32m✓\033[0m" else "\033[31m✗\033[0m"
  cat("  ", mark, " ", label, if (nzchar(detail)) paste0("  (", detail, ")"), "\n", sep = "")
  if (!ok) problems <<- problems + 1
}

cat("R\n")
report(getRversion() >= "4.1", R.version.string, "need 4.1+")

cat("\nPackages\n")
# diabetes.R only uses base R; renv is for the dependency-management section.
for (pkg in c("renv")) {
  if (requireNamespace(pkg, quietly = TRUE)) {
    report(TRUE, paste(pkg, packageVersion(pkg)))
  } else {
    report(FALSE, paste(pkg, "missing"), sprintf('run: install.packages("%s")', pkg))
  }
}

cat("\nGit\n")
if (nzchar(Sys.which("git"))) {
  report(TRUE, system("git --version", intern = TRUE))
  for (key in c("user.name", "user.email")) {
    value <- suppressWarnings(system(paste("git config --global", key), intern = TRUE))
    ok <- length(value) > 0 && nzchar(value[1])
    report(ok, paste("git config", key),
           if (ok) value[1] else sprintf('run: git config --global %s "..."', key))
  }
} else {
  report(FALSE, "git not installed", "https://git-scm.com/downloads")
}

cat("\n")
if (problems > 0) {
  cat(problems, "problem(s) found. See the Setup section of README.md.\n")
  quit(status = 1)
}
cat("All set! See you at the workshop.\n")
