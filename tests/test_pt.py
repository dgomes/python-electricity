import pytest
from datetime import datetime
from electricity.tariffs import EDP, Galp, Operators 


def test_tariffs_edp():
    edp = EDP(plan="Bi-horário - ciclo diário")
    assert "Cheias" in edp.available_tariffs()
    assert "Vazio" in edp.available_tariffs()

    assert "Tri-horário - ciclo semanal" not in Galp.tariff_periods()

    weekday_summer = datetime(2019, 7, 8, 9, 30)
    assert edp.tri_horario_diario(weekday_summer) == "Cheias"
    assert edp.tri_horario_semanal(weekday_summer) == "Ponta"
    assert edp.bi_horario_diario(weekday_summer) == "Fora de Vazio"
    assert edp.bi_horario_semanal(weekday_summer) == "Fora de Vazio"

    weekday_winter = datetime(2019, 1, 2, 9, 30)
    assert edp.tri_horario_diario(weekday_winter) == "Ponta"
    assert edp.tri_horario_semanal(weekday_winter) == "Ponta"
    assert edp.bi_horario_diario(weekday_winter) == "Fora de Vazio"
    assert edp.bi_horario_semanal(weekday_winter) == "Fora de Vazio"

    # TODO write more exaustive tests
