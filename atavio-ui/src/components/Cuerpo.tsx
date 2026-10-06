import * as React from 'react';

export interface CuerpoProps extends React.HTMLAttributes<HTMLParagraphElement> {
  children?: React.ReactNode;
  /** «cuerpo» 36 px (mínimo para texto corrido) o «nota» 28 px (pies y aclaraciones, nunca menos). */
  tamano?: 'cuerpo' | 'nota';
}

/** Texto corrido en Libre Franklin; toma el color de texto del fondo de la Lamina (tinta sobre hueso y molde, hueso sobre ladrillo y tinta). */
export function Cuerpo({ children, tamano = 'cuerpo', className, ...rest }: CuerpoProps) {
  return (
    <p {...rest} className={['atv-cuerpo', tamano === 'nota' ? 'atv-cuerpo-nota' : '', className].filter(Boolean).join(' ')}>
      {children}
    </p>
  );
}
