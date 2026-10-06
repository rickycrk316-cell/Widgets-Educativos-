import * as React from 'react';
import { sellos } from '../assets/sellos';

export type SelloVariante =
  | 'principal' | 'reducido'
  | 'invertido' | 'invertido-reducido'
  | 'tinta' | 'tinta-reducido'
  | 'hueso' | 'hueso-reducido';

export interface SelloProps extends Omit<React.SVGAttributes<SVGSVGElement>, 'width' | 'height'> {
  /** Versión del logo. «principal» lleva la bajada «LA TIENDA DE LA FÁBRICA» (mínimo 172 px); «reducido» no (mínimo 64 px recomendado, 48 absoluto). «invertido» (círculo hueso, letras rojas) solo sobre ladrillo; «tinta» y «hueso» son de una tinta. */
  variante?: SelloVariante;
  /** Diámetro en px. */
  tamano?: number;
  /** Texto accesible. */
  titulo?: string;
}

/** Sello de ATAVÍO: círculo relleno #DA3732 con el nombre en blanco; es el único logo y el único uso del rojo sello. */
export function Sello({ variante = 'principal', tamano = 200, titulo = 'Atavío', className, ...rest }: SelloProps) {
  const a = sellos[variante] ?? sellos.principal;
  return (
    <svg
      {...rest}
      className={['atv-svg', 'atv-sello', className].filter(Boolean).join(' ')}
      xmlns="http://www.w3.org/2000/svg"
      viewBox={a.viewBox}
      width={tamano}
      height={tamano}
      role="img"
      aria-label={titulo}
      dangerouslySetInnerHTML={{ __html: a.inner }}
    />
  );
}
