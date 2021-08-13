$venv = ".venv"

function Use-Environment() {
  Write-Host "Activating python virtual environment '$($venv)'"
  . "$($venv)/scripts/activate"
}

if(!(Test-Path $venv)) {
  Write-Host "Creating python virtual environment '$($venv)'"
  py -m venv $venv

  Use-Environment

  Write-Host "Installing requirements"
  pip install -r requirements.txt
} else {
  Use-Environment
}
