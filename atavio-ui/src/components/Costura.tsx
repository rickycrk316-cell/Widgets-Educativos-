import * as React from 'react';

export type ColorCostura = 'ladrillo' | 'hueso' | 'molde' | 'tinta';
const COLORES: Record<ColorCostura, string> = {
  ladrillo: '#A31A0E', hueso: '#F3EDE1', molde: '#C8A97E', tinta: '#2B2B2B',
};

export interface CosturaProps extends Omit<React.SVGAttributes<SVGSVGElement>, 'width' | 'height' | 'color'> {
  /** Largo de la hebra en px. En un carrusel usa 1080 (o 2160 si cruza dos láminas) para que empate en el borde. */
  largo?: number;
  /** Dirección de la hebra. */
  orientacion?: 'horizontal' | 'vertical';
  /** Color de la hebra: ladrillo sobre hueso o molde; hueso o molde sobre ladrillo y tinta. */
  color?: ColorCostura;
  /** Grosor del trazo en px (4,5 por defecto; un solo grosor por pieza). */
  grosor?: number;
}

/** Costura continua: pespunte punteado (guion 9 px, espacio 6 px) que recorre la pieza; una sola por pieza. */
export function Costura({ largo = 1080, orientacion = 'horizontal', color = 'ladrillo', grosor = 4.5, className, ...rest }: CosturaProps) {
  const alto = 40;
  const v = orientacion === 'vertical';
  const w = v ? alto : largo;
  const h = v ? largo : alto;
  const d = v ? `M${alto / 2} 5.25V${largo - 5.25}` : `M5.25 ${alto / 2}H${largo - 5.25}`;
  return (
    <svg
      {...rest}
      className={['atv-svg', 'atv-costura', className].filter(Boolean).join(' ')}
      xmlns="http://www.w3.org/2000/svg"
      viewBox={`0 0 ${w} ${h}`}
      width={w}
      height={h}
      fill="none"
      aria-hidden="true"
    >
      <path d={d} stroke={COLORES[color]} strokeWidth={grosor} strokeLinecap="round" strokeLinejoin="round" strokeDasharray="4.5 10.5" />
    </svg>
  );
}
