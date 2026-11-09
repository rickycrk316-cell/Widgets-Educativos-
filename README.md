# Widgets educativos · Quirúrgica 2 (PUCE, 10.º nivel)

Widgets HTML de estudio, autocontenidos y offline. Los nuevos siguen **v11** (`docs/DECISIONES_v11.md`, skill `widget-ensenanza` en `.claude/skills/`, kit `kit/v11/`): regla 20/80 (núcleo arriba, detalle debajo), perlas de examen (PUCE, CACES, USMLE 1/2, MIR, ENARM), ordenar pasos como recuerdo activo, estilo app con acento por tema, barra inferior en iPhone y menú lateral en iPad y Mac. Los widgets anteriores son v10.2 (kit «Vademécum», legado) y no se tocan. Abre el `.html` de cada tema en el navegador o en Archivos del iPad.

## Widgets

| Tema | Widget (HTML) | Modo | Entidades | Marcas pendientes (legado) |
|---|---|---|---|---|
| Dolor abdominal | `Abdomen_agudo_quirurgico_widget_v10.html` | multi | apendicitis (principal), obstrucción, perforación, isquemia mesentérica, AAA roto (amenaza) | 42 |
| | `Dolor_biliopancreatico_widget_v10.html` | multi | colelitiasis/colecistitis (principal), coledocolitiasis, colangitis (amenaza), pancreatitis | 85 |
| | `Abdomen_agudo_medico_widget_v10.html` | multi | hipopotasemia con íleo (principal), saturnismo, porfiria aguda (amenaza) | 17 |
| Neoplasias GI | `Cancer_digestivo_alto_widget_v10.html` | multi | gástrico (principal y amenaza), cavidad oral, esófago, duodeno | 113 |
| | `Cancer_hepatobiliopancreatico_widget_v10.html` | multi | páncreas (principal y amenaza), hepatocelular, vesícula, colangiocarcinoma | 7 |
| | `Cancer_colorrectal_widget_v10.html` | mono | + pestaña de tamizaje y lesiones premalignas | 62 |
| Patología urinaria baja | `Patologia_urinaria_baja_widget_v10.html` | multi | HPB (principal), prostatitis, cáncer de próstata (amenaza), cistitis, uretritis · caso de Carlos | 38 |
| | `Prostatitis_cistitis_cancer_vesical_widget_v10.html` | multi | cistitis infecciosa (principal), prostatitis (amenaza), cáncer vesical | 15 |
| | `Cancer_de_prostata_widget_v10.html` | mono | cáncer de próstata | 7 |
| | `Definiciones_patologia_urinaria_baja.html` | definiciones | 9 términos + repaso | 0 |
| Disbasia infantil | `Cojera_dolorosa_sistemica_widget_v10.html` | multi | sinovitis transitoria (principal), artritis séptica (amenaza), osteomielitis, neoplasia ósea | 27 |
| | `Cojera_dolorosa_mecanica_widget_v10.html` | multi | Perthes (principal), epifisiólisis (amenaza), Osgood-Schlatter | 27 |
| | `Marcha_sin_dolor_widget_v10.html` | multi | DDC (principal), dismetría, neuromuscular, Guillain-Barré (amenaza) | 65 |
| | `Forma_piernas_pies_widget_v10.html` | multi | genu varo/valgo (principal), anteversión femoral, pie plano, pie cavo, equinovaro (amenaza) | 26 |
| Trastornos del ánimo | `Crisis_de_angustia_widget_v10.html` | multi | trastorno de pánico (principal), ansiedad generalizada, depresión mayor, consumo de benzodiacepinas, síndrome coronario agudo (amenaza) | 0 |
| | `Apertura_trastornos_animo.html` | apertura | caso + 9 términos, 12 problemas (B, P, S, FR), jerarquización, 4 hipótesis, repaso | 1 (composición de Stresstabs) |
| | `Depresion_bipolar_suicidio_widget_v11.html` | v11 · multi | depresión mayor (principal), trastorno bipolar, conducta suicida (amenaza) · núcleo por pestaña, 20 perlas de examen, ejercicio Ordenar (10 bloques), visión de conjunto en preguntas, referencias enlazadas | 0 |
| Ginecología (sin sílabo) | `Ciclo_ovarico_menopausia_TH_widget_v11.html` | v11 · mono (piloto) | menopausia y terapia hormonal + pestaña «Ciclo ovárico y cuerpo albo»: núcleo por pestaña, perlas por examen, ordenar pasos | 0 |

«Marcas pendientes (legado)» = datos marcados `[VERIFICAR EN FUENTE]` en widgets v10.2 anteriores a la regla de cero marcas: compruébalos antes de estudiar con ellos. Los widgets v11 y las definiciones/aperturas nuevas no llevan marcas: lo no confirmado se elimina.

## Estructura

```
widgets/<tema>/PLAN.md          partición del caso en widgets y decisión del router
widgets/<tema>/*.html           widgets finales (generados: no editar a mano)
widgets/<tema>/<id>/            partes numeradas + manifiesto.json (aquí se edita)
kit/v11/                        kit v11: cabecera, script, validador y prueba de navegador
kit/                            kit v10.2 (legado), ensamblador construir.py y validadores
.claude/skills/                 widget-ensenanza (v11), definiciones, apertura, impeccable (revisión opcional)
fuentes/                        sílabos (dos rotaciones), contratos de definiciones y apertura, protocolo de verificación, casos
docs/                           DECISIONES_v11.md (fuente de verdad), PRODUCT.md (propósito), DESIGN.md (sistema visual)
```

## Reconstruir y validar

```sh
python3 kit/construir.py                          # todos (elige el kit por "tipo" del manifiesto)
python3 kit/construir.py widgets/ginecologia/menopausia_th
python3 kit/renumerar.py widgets/<tema>/<id>      # citas Vancouver por primera aparición
node kit/v11/probar.js file://$PWD/widgets/<tema>/<widget>.html /tmp/capturas        # widgets v11
node kit/probar_navegador.js file://$PWD/widgets/<tema>/<widget>.html /tmp/capturas  # legado multi/mono
```

Requiere `python3` con `beautifulsoup4` (se instala solo) y `node` (`cd kit && npm ci` una vez). Las pruebas de navegador usan Playwright con el Chromium de `/opt/pw-browsers`.
