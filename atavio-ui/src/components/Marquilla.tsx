import * as React from 'react';
import { motivos } from '../assets/motivos';
import type { Tono } from './tipos';

export interface MarquillaProps extends React.HTMLAttributes<HTMLDivElement> {
  /** Nombre de la serie, corto (2 a 3 palabras), p. ej. «Voltéala». Se escribe en mayúsculas. */
  children?: React.ReactNode;
  /** Ancho en px (el alto es 0,48 veces el ancho). */
  ancho?: number;
  /** «claro»: texto hueso sobre ladrillo; «oscuro»: texto tinta sobre hueso. */
  tono?: Tono;
}

/** Marquilla de serie: etiqueta cosida pequeña con el nombre de la serie, solo en portadas de serie, nunca sobre cada titular. */
export function Marquilla({ children, ancho = 320, tono = 'claro', className, style, ...rest }: MarquillaProps) {
  const a = motivos[`marquilla-${tono}`];
  return (
    <div {...rest} className={['atv-marquilla', className].filter(Boolean).join(' ')} style={{ width: ancho, ...style }}>
      <svg xmlns="http://www.w3.org/2000/svg" viewBox={a.viewBox} fill="none" aria-hidden="true" dangerouslySetInnerHTML={{ __html: a.inner }} />
      <div className="atv-marquilla-texto"
        style={{ left: '29.7%', width: '54.1%', top: '32.3%', height: '36.1%', fontSize: ancho * 0.075, color: tono === 'claro' ? '#F3EDE1' : '#2B2B2B' }}>
        {children}
      </div>
    </div>
  );
}
