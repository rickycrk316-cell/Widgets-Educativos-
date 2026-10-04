#!/bin/sh
cd "$(dirname "$0")"
cat parts/p00_head.html parts/p01_nav.html parts/p10_t1.html parts/p20_t2.html parts/p30_t3.html parts/p40_t4.html parts/p50_t5.html parts/p60_t6.html parts/p70_t7.html parts/p80_t8.html parts/p90_t9.html parts/p95_tg.html parts/p96_js.html > widget.html
