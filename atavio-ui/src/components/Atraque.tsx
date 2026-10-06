import * as React from 'react';
import { motivos } from '../assets/motivos';
import type { Tono } from './tipos';

export interface AtraqueProps extends Omit<React.SVGAttributes<SVGSVGElement>, 'width' | 'height'> {
  /** Lado en px (el dibujo es cuadrado). */
  tamano?: number;
  /** «claro» (para hueso o molde) u «oscuro» (para tinta o ladrillo). */
  tono?: Tono;
}

/** Atraque en X ampliado sobre tela: el refuerzo de puntadas apretadas donde más se jala; detalle de oficio para hablar de durabilidad. */
export function Atraque({ tamano = 400, tono = 'claro', className, ...rest }: AtraqueProps) {
  const a = motivos[`atraque-${tono}`];
  return (
    <svg
      {...rest}
      className={['atv-svg', 'atv-atraque', className].filter(Boolean).join(' ')}
      xmlns="http://www.w3.org/2000/svg"
      viewBox={a.viewBox}
      width={tamano}
      height={tamano}
      fill="none"
      role="img"
      aria-label="Atraque en X"
      dangerouslySetInnerHTML={{ __html: a.inner }}
    />
  );
}
